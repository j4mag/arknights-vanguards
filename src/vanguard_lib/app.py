import argparse
import pathlib
import typing
import pydantic
import plotly.graph_objects as go
import json
import yattag

from . import api
from . import vanguards
from . import simulation
from . import plotting


class SimulationParameters(pydantic.BaseModel):
    operators: list[api.Vanguard]
    t_step: float = 0.1
    t_end: float = 240
    dp_start: float = 0
    title: str = ""

    plot_dp_absolute: bool = True
    plot_dp_added: bool = True
    plot_dp_added_trend: bool = True
    plot_dp_relative: bool = True


class Parameters(pydantic.BaseModel):
    simulations: list[SimulationParameters]
    output_dir: pathlib.Path = pathlib.Path("output")


def get_parameters(config_path: pathlib.Path | None) -> Parameters:
    if config_path:
        with open(config_path, encoding="utf-8") as f:
            config_json = json.load(f)
        return Parameters.model_validate(config_json)

    return Parameters(
        simulations=[
            SimulationParameters(
                operators=vanguards.ALL_OPERATOR_SKILLS,
                title="All Operators",
                t_step=0.1,
                t_end=240,
                dp_start=0,
                plot_dp_absolute=True,
                plot_dp_added=True,
                plot_dp_added_trend=True,
                plot_dp_relative=True,
            ),
            SimulationParameters(
                operators=vanguards.ALL_OPERATOR_SKILLS,
                title="All Operators",
                t_step=0.1,
                t_end=240,
                dp_start=20,
                plot_dp_absolute=False,
                plot_dp_added=True,
                plot_dp_added_trend=True,
                plot_dp_relative=True,
            ),
            SimulationParameters(
                operators=[
                    vanguards.OPERATOR_MYRTLE[0],
                    vanguards.OPERATOR_ELYSIUM[1],
                    vanguards.OPERATOR_VULPISFOGLIA[1],
                    vanguards.OPERATOR_VULPISFOGLIA[2],
                    # OPERATOR_VULPISFOGLIA_Y1[1], # Y1, S2M3, P1
                    # OPERATOR_VULPISFOGLIA_Y1[2], # Y1, S3S3, P1
                    vanguards.OPERATOR_VULPISFOGLIA_Y1[3],  # Y1, S2M3, P6
                ],
                title="Vulpisfoglia",
                t_step=0.1,
                t_end=240,
                dp_start=0,
                plot_dp_absolute=False,
                plot_dp_added=True,
                plot_dp_added_trend=True,
                plot_dp_relative=True,
            ),
            SimulationParameters(
                operators=sum(vanguards.OPERATORS_FLAGBEARERS, start=[]),
                title="Flagbearers",
                t_step=0.1,
                t_end=240,
                dp_start=0,
                plot_dp_absolute=False,
                plot_dp_added=True,
                plot_dp_added_trend=True,
                plot_dp_relative=True,
            ),
            SimulationParameters(
                operators=sum(vanguards.OPERATORS_PIONEERS, start=[]),
                title="Pioneers",
                t_step=0.1,
                t_end=240,
                dp_start=0,
                plot_dp_absolute=False,
                plot_dp_added=True,
                plot_dp_added_trend=True,
                plot_dp_relative=True,
            ),
            SimulationParameters(
                operators=sum(vanguards.OPERATORS_TACTICIANS, start=[]),
                title="Tacticians",
                t_step=0.1,
                t_end=240,
                dp_start=0,
                plot_dp_absolute=False,
                plot_dp_added=True,
                plot_dp_added_trend=True,
                plot_dp_relative=True,
            ),
            SimulationParameters(
                operators=[
                    vanguards.OPERATOR_MYRTLE[0],
                    *sum(vanguards.OPERATORS_AGENTS, start=[]),
                ],
                title="Agents",
                t_step=0.1,
                t_end=240,
                dp_start=0,
                plot_dp_absolute=False,
                plot_dp_added=True,
                plot_dp_added_trend=False,
                plot_dp_relative=True,
            ),
        ]
    )


def simulate_and_plot(sim_params: SimulationParameters) -> list[go.Figure]:
    figs = []
    results = simulation.simulate_operators(
        sim_params.operators, sim_params.t_step, sim_params.t_end, sim_params.dp_start
    )
    if sim_params.plot_dp_absolute:
        figs.append(plotting.plot_dp_absolute(results, sim_params.title))
    if sim_params.plot_dp_added:
        figs.append(plotting.plot_dp_added(results, sim_params.title))
    if sim_params.plot_dp_added_trend:
        figs.append(plotting.plot_dp_added_trend(results, sim_params.title))
    if sim_params.plot_dp_relative:
        figs.append(plotting.plot_dp_relative(results, sim_params.title))
    return figs


def run(params: Parameters):
    params.output_dir.mkdir(exist_ok=True)
    with open(params.output_dir / "config.json", "w", encoding="utf-8") as f:
        config_json = params.model_dump_json(indent=4, round_trip=True)
        f.write(config_json)

    figures = sum(
        (simulate_and_plot(sim_params) for sim_params in params.simulations),
        start=[],
    )
    figure_paths = [
        (plotting.save_plot(fig, tgt_dir=params.output_dir / "plots", mkdir=True), fig)
        for fig in figures
    ]

    write_index(params.output_dir / "index.html", figure_paths)


def write_index(
    tgt_file: pathlib.Path,
    figure_paths: typing.Sequence[tuple[pathlib.Path, go.Figure]],
):
    doc = yattag.Doc()
    with doc.tag("h1"):
        doc.text("Arknights Vanguard Index")
    for path, fig in figure_paths:
        with doc.tag("p"):
            with doc.tag("a", href=str(path.relative_to(tgt_file.parent))):
                title = plotting._get_fig_name(fig, default="Unnamed Figure")
                doc.text(title.replace("<br>", "\u2013"))

    with open(tgt_file, "w", encoding="utf-8") as f:
        f.write(doc.getvalue())


def main(argv: typing.Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config-file",
        type=pathlib.Path,
        required=False,
        help="Path to configuration files",
    )
    args = parser.parse_args(argv)
    params = get_parameters(args.config_file)
    run(params)
    return 0
