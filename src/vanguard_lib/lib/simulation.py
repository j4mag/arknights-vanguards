import plotly
import itertools
import numpy as np

from . import api


## SIMULATION
def simulate(
    setup: api.SimulationSetup,
) -> api.SimulationResult:
    _epsilon = 1e-12  # small fudge factor to overcome floating point inequality (e.g. 0.300004 != 0.3)

    # state
    t = np.arange(0, setup.time_end, setup.time_step)
    dp = np.zeros_like(t)
    is_operator_deployed = False
    has_talent_triggered = False
    skill_active = False
    sp = 0
    for i in range(len(dp)):
        if i == 0:
            dp[i] += setup.dp_start
            continue

        # region natural dp generation
        dp[i] = dp[i - 1] + setup.time_step * setup.dp_per_second

        if setup.operator is None:
            continue

        # region deployment logic
        if not is_operator_deployed and dp[i] >= setup.operator.cost:
            is_operator_deployed = True
            sp = setup.operator.skill.initial_sp
            dp[i] -= setup.operator.cost
            continue

        # region talents
        if isinstance(setup.operator.talent, api.DPTalent):
            if (
                (is_operator_deployed or not setup.operator.talent.needs_to_be_deployed)
                and not has_talent_triggered
                and setup.operator.talent.dp_to_trigger <= dp[i]
            ):
                has_talent_triggered = True
                dp[i] += setup.operator.talent.dp_on_trigger

        if isinstance(setup.operator.talent, api.DPRegenTalent):
            if is_operator_deployed or not setup.operator.talent.needs_to_be_deployed:
                dp[i] += setup.operator.talent.dp_per_second * setup.time_step

        if not is_operator_deployed:
            continue

        # region skill
        if sp < setup.operator.skill.sp_cost:
            sp += setup.operator.skill.sp_per_second * setup.time_step + _epsilon
        else:
            # skill duration is also tracked by 'sp', though it ignores sp-per-second buffs
            sp += setup.time_step + _epsilon

        if sp >= setup.operator.skill.sp_cost:
            if setup.operator.skill.duration == 0:
                # instantaneous skill trigger
                dp[i] += setup.operator.skill.total_dp_generation
                sp -= setup.operator.skill.sp_cost

            elif sp < setup.operator.skill.sp_cost + setup.operator.skill.duration:
                # duration skill in progress
                if setup.operator.skill.instant:
                    if not skill_active:
                        dp[i] += setup.operator.skill.total_dp_generation
                else:
                    dp[i] += (
                        setup.operator.skill.total_dp_generation
                        / setup.operator.skill.duration
                        * setup.time_step
                    )
                skill_active = True

            else:
                # duration skill ends
                sp -= setup.operator.skill.sp_cost + setup.operator.skill.duration
                skill_active = False

    return api.SimulationResult(name=setup.name, setup=setup, t=t, dp=dp)


def simulate_operators(
    operators: list[api.Vanguard], t_step=0.1, t_end=240, dp_start=0
) -> list[api.SimulationResult]:
    simulation_setups = [
        api.SimulationSetup(
            name=f"{operator.name} | {operator.skill.name}",
            operator=operator,
            time_step=t_step,
            time_end=t_end,
            dp_start=dp_start,
            color=color,
        )
        for operator, color in zip(
            operators, itertools.cycle(plotly.colors.DEFAULT_PLOTLY_COLORS)
        )  # assign consistent colors for all plots
    ]
    return [simulate(sim) for sim in simulation_setups]
