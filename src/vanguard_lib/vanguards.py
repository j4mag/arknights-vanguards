from . import api

## OPERATORS

# All hand-entered from arknights.wiki.gg
# I haven't been accounting for cast time on "instant" skills
#   like Texas S2, 'next attack'-type, etc.  Those may be over-scored.

#! To add a new operator, e.g. Siege:
# 1. add a new list 'OPERATOR_SIEGE', with each skill of interest, following the patterns below
# 2. add them to their archetype's list, e.g. OPERATORS_PIONEERS
# 3. 'Run All' cells in the jupyter notebook, find or create a set of plots which include them

OPERATOR_MYRTLE = [
    api.Vanguard(
        name="Myrtle P6",
        cost=8,
        skill=api.Skill(
            name="S1M3 - Support β",
            initial_sp=13,
            sp_cost=22,
            duration=8,
            total_dp_generation=14,
        ),
    ),
    api.Vanguard(
        name="Myrtle P6",
        cost=8,
        skill=api.Skill(
            name="S2M3 - Healing Wings",
            initial_sp=10,
            sp_cost=24,
            duration=16,
            total_dp_generation=16,
        ),
    ),
]
OPERATOR_ELYSIUM = [
    api.Vanguard(
        name="Elysium P6",
        cost=9,
        skill=api.Skill(
            name="S1M3 - Support γ",
            initial_sp=15,
            sp_cost=26,
            duration=8,
            total_dp_generation=18,
        ),
        talent=api.DPTalent(
            name="Sniper Support E2",
            dp_to_trigger=11,  # to deploy a 13dp sniper
            dp_on_trigger=2,
        ),
    ),
    api.Vanguard(
        name="Elysium P6",
        cost=9,
        skill=api.Skill(
            name="S2M3 - Monitor",
            initial_sp=16,
            sp_cost=30,
            duration=15,
            total_dp_generation=20,
        ),
        talent=api.DPTalent(
            name="Sniper Support E2",
            dp_to_trigger=11,  # to deploy a 13dp sniper
            dp_on_trigger=2,
        ),
    ),
]
OPERATOR_WANQING = [
    api.Vanguard(
        name="Wanqing P6",
        cost=10,
        skill=api.Skill(
            name="S1M3 - Support γ",
            initial_sp=15,
            sp_cost=26,
            duration=8,
            total_dp_generation=18,
        ),
    ),
    api.Vanguard(
        name="Wanqing P6",
        cost=10,
        skill=api.Skill(
            name="S2M3 - Along the Easterlies",
            initial_sp=16,
            sp_cost=30,
            duration=15,
            total_dp_generation=20,
        ),
    ),
]
OPERATOR_SAILEACH = [
    api.Vanguard(
        name="Saileach P1",
        cost=12,
        skill=api.Skill(
            name="S1M3 - Support γ",
            initial_sp=15,
            sp_cost=26,
            duration=8,
            total_dp_generation=18,
        ),
        talent=api.DPTalent(
            name="Spiritual Influence",
            dp_to_trigger=11,  # to deploy a 13dp sniper
            dp_on_trigger=2,
        ),
    ),
    api.Vanguard(
        name="Saileach P1",
        cost=12,
        skill=api.Skill(
            name="S2M3 - Inheritance of Faith",
            initial_sp=5,
            sp_cost=29,
            duration=15,
            total_dp_generation=20,
        ),
        talent=api.DPTalent(
            name="Spiritual Influence",
            dp_to_trigger=11,  # to deploy a 13dp sniper
            dp_on_trigger=2,
        ),
    ),
    api.Vanguard(
        name="Saileach P1",
        cost=12,
        skill=api.Skill(
            name="S3M3 - Glorious Banner",
            initial_sp=7,
            sp_cost=20,
            duration=10,
            total_dp_generation=10,
            instant=True,
        ),
        talent=api.DPTalent(
            name="Spiritual Influence",
            dp_to_trigger=11,  # to deploy a 13dp sniper
            dp_on_trigger=2,
        ),
    ),
]
OPERATORS_FLAGBEARERS = [
    OPERATOR_MYRTLE,
    OPERATOR_WANQING,
    OPERATOR_ELYSIUM,
    OPERATOR_SAILEACH,
]

OPERATOR_TEXAS = [
    api.Vanguard(
        name="Texas P6",
        cost=11,
        skill=api.Skill(
            name="S1M3 - Charge γ",
            initial_sp=20,
            sp_cost=35,
            duration=0,
            total_dp_generation=12,
        ),
        talent=api.DPTalent(
            name="Tactical Delivery E2",
            dp_to_trigger=0,
            dp_on_trigger=2,
            needs_to_be_deployed=False,
        ),
    ),
    api.Vanguard(
        name="Texas P6",
        cost=11,
        skill=api.Skill(
            name="S2M3 - Sword Rain",
            initial_sp=30,
            sp_cost=40,
            duration=0,
            total_dp_generation=12,
        ),
        talent=api.DPTalent(
            name="Tactical Delivery E2",
            dp_to_trigger=0,
            dp_on_trigger=2,
            needs_to_be_deployed=False,
        ),
    ),
]
OPERATOR_TEXAS_Y3 = [
    api.Vanguard(
        name="Texas P6 modY3",
        cost=7,
        skill=api.Skill(
            name="S1M3 - Charge γ",
            initial_sp=20,
            sp_cost=35,
            duration=0,
            total_dp_generation=12,
        ),
        talent=api.DPTalent(
            name="Tactical Delivery E2",
            dp_to_trigger=0,
            dp_on_trigger=2,
            needs_to_be_deployed=False,
        ),
    ),
    api.Vanguard(
        name="Texas P6 modY3",
        cost=7,
        skill=api.Skill(
            name="S2M3 - Sword Rain",
            initial_sp=30,
            sp_cost=40,
            duration=0,
            total_dp_generation=12,
        ),
        talent=api.DPTalent(
            name="Tactical Delivery E2",
            dp_to_trigger=0,
            dp_on_trigger=2,
            needs_to_be_deployed=False,
        ),
    ),
]
OPERATOR_SIEGE = [
    api.Vanguard(
        name="Siege P1",
        cost=7,
        skill=api.Skill(
            name="S1M3 - Charge γ",
            initial_sp=20,
            sp_cost=35,
            duration=0,
            total_dp_generation=12,
        ),
    ),
    api.Vanguard(
        name="Siege P1",
        cost=7,
        skill=api.Skill(
            name="S2M3 - Aerial Hammer",
            initial_sp=10,
            sp_cost=10,
            duration=0,
            total_dp_generation=3,
        ),
    ),
    api.Vanguard(
        name="Siege P1",
        cost=7,
        skill=api.Skill(
            name="S3M3 - Skull Breaker",  # lol
            initial_sp=25,
            sp_cost=30,
            duration=25,
            total_dp_generation=0,
        ),
    ),
]
OPERATOR_SAGA = [
    api.Vanguard(
        name="Saga P1",
        cost=14,
        skill=api.Skill(
            name="S1M3 - Charge γ",
            initial_sp=20,
            sp_cost=35,
            duration=0,
            total_dp_generation=12,
        ),
    ),
    api.Vanguard(
        name="Saga P1",
        cost=14,
        skill=api.Skill(
            name="S2M3 - Cleansing Evil (no kills)",
            initial_sp=10,
            sp_cost=13,
            duration=0,
            total_dp_generation=4,
        ),
    ),
    api.Vanguard(
        name="Saga P1",
        cost=14,
        skill=api.Skill(
            name="S3M3 - Fierce Glare",
            initial_sp=28,
            sp_cost=40,
            duration=20,
            total_dp_generation=20,
        ),
    ),
]
OPERATOR_SAGA_Y3 = [
    api.Vanguard(
        name="Saga P1 modY3",
        cost=10,
        skill=api.Skill(
            name="S1M3 - Charge γ",
            initial_sp=20,
            sp_cost=35,
            duration=0,
            total_dp_generation=12,
        ),
    ),
    api.Vanguard(
        name="Saga P1 modY3",
        cost=10,
        skill=api.Skill(
            name="S2M3 - Cleansing Evil (no kills)",
            initial_sp=10,
            sp_cost=13,
            duration=0,
            total_dp_generation=4,
        ),
    ),
    api.Vanguard(
        name="Saga P1 modY3",
        cost=10,
        skill=api.Skill(
            name="S3M3 - Fierce Glare",
            initial_sp=28,
            sp_cost=40,
            duration=20,
            total_dp_generation=20,
        ),
    ),
]
OPERATOR_FLAMETAIL = [
    api.Vanguard(
        name="Flametail P1",
        cost=14,
        skill=api.Skill(
            name="S1M3 - Quick Intuition",
            initial_sp=9,
            sp_cost=18,
            duration=0,
            total_dp_generation=6,
        ),
    ),
    api.Vanguard(
        name="Flametail P1",
        cost=14,
        skill=api.Skill(
            name="S2M3 - 'Pinus Sylvestris'",
            initial_sp=30,
            sp_cost=40,
            duration=0,
            total_dp_generation=13,
        ),
    ),
    api.Vanguard(
        name="Flametail P1",
        cost=14,
        skill=api.Skill(
            name="S3M3 - Flameheart",
            initial_sp=6,
            sp_cost=16,
            duration=8,
            total_dp_generation=8,
        ),
    ),
]
OPERATOR_FLAMETAIL_Y3 = [
    api.Vanguard(
        name="Flametail P1 modY3",
        cost=10,
        skill=api.Skill(
            name="S1M3 - Quick Intuition",
            initial_sp=9,
            sp_cost=18,
            duration=0,
            total_dp_generation=6,
        ),
    ),
    api.Vanguard(
        name="Flametail P1 modY3",
        cost=10,
        skill=api.Skill(
            name="S2M3 - 'Pinus Sylvestris'",
            initial_sp=30,
            sp_cost=40,
            duration=0,
            total_dp_generation=13,
        ),
    ),
    api.Vanguard(
        name="Flametail P1 modY3",
        cost=10,
        skill=api.Skill(
            name="S3M3 - Flameheart",
            initial_sp=6,
            sp_cost=16,
            duration=8,
            total_dp_generation=8,
        ),
    ),
]
OPERATOR_VULPISFOGLIA = [
    api.Vanguard(
        name="Vulpisfoglia P1",
        cost=14,
        skill=api.Skill(
            name="S1M3 - Light Punishment",
            initial_sp=8,
            sp_cost=4,
            duration=0,
            total_dp_generation=1,
        ),
        talent=api.DPRegenTalent(
            name="Gathering Momentum",
            dp_per_second=0.1,
        ),
    ),
    api.Vanguard(
        name="Vulpisfoglia P1",
        cost=14,
        skill=api.Skill(
            name="S2M3 - Light Bladefall Torture",
            initial_sp=20,
            sp_cost=20,
            duration=0,
            total_dp_generation=7,
        ),
        talent=api.DPRegenTalent(
            name="Gathering Momentum",
            dp_per_second=0.1,
        ),
    ),
    api.Vanguard(
        name="Vulpisfoglia P1",
        cost=14,
        skill=api.Skill(
            name="S3M3 - Volpombra Technique",
            initial_sp=10,
            sp_cost=18,
            duration=10,
            total_dp_generation=9,
            instant=True,
        ),
        talent=api.DPRegenTalent(
            name="Gathering Momentum",
            dp_per_second=0.1,
        ),
    ),
]
OPERATOR_VULPISFOGLIA_Y1 = [
    api.Vanguard(
        name="Vulpisfoglia P1 modY1 (Unreleased)",
        cost=10,
        skill=api.Skill(
            name="S1M3 - Light Punishment",
            initial_sp=8,
            sp_cost=4,
            duration=0,
            total_dp_generation=1,
        ),
        talent=api.DPRegenTalent(
            name="Gathering Momentum",
            dp_per_second=0.1,
        ),
    ),
    api.Vanguard(
        name="Vulpisfoglia P1 modY1 (Unreleased)",
        cost=10,
        skill=api.Skill(
            name="S2M3 - Light Bladefall Torture",
            initial_sp=20,
            sp_cost=20,
            duration=0,
            total_dp_generation=7,
        ),
        talent=api.DPRegenTalent(
            name="Gathering Momentum",
            dp_per_second=0.1,
        ),
    ),
    api.Vanguard(
        name="Vulpisfoglia P1 modY1 (Unreleased)",
        cost=10,
        skill=api.Skill(
            name="S3M3 - Volpombra Technique",
            initial_sp=10,
            sp_cost=18,
            duration=10,
            total_dp_generation=9,
            instant=True,
        ),
        talent=api.DPRegenTalent(
            name="Gathering Momentum",
            dp_per_second=0.1,
        ),
    ),
    api.Vanguard(
        name="Vulpisfoglia P6 modY1 (Unreleased)",
        cost=8,
        skill=api.Skill(
            name="S2M3 - Light Bladefall Torture",
            initial_sp=20,
            sp_cost=20,
            duration=0,
            total_dp_generation=7,
        ),
        talent=api.DPRegenTalent(
            name="Gathering Momentum",
            dp_per_second=0.1,
        ),
    ),
]
OPERATORS_PIONEERS = [
    OPERATOR_TEXAS,
    OPERATOR_TEXAS_Y3,
    OPERATOR_SIEGE,
    OPERATOR_SAGA,
    OPERATOR_SAGA_Y3,
    OPERATOR_FLAMETAIL,
    OPERATOR_FLAMETAIL_Y3,
    OPERATOR_VULPISFOGLIA,
    OPERATOR_VULPISFOGLIA_Y1,
]

OPERATOR_BEANSTALK = [
    api.Vanguard(
        name="Beanstalk P6",
        cost=11,
        skill=api.Skill(
            name="S1M3 - Sentinel Command",
            initial_sp=15,
            sp_cost=30,
            duration=0,
            total_dp_generation=8,
            instant=True,
        ),
    ),
    api.Vanguard(
        name="Beanstalk P6",
        cost=11,
        skill=api.Skill(
            name="S2M3 - 'Everyone Together!'",
            initial_sp=18,
            sp_cost=40,
            duration=15,
            total_dp_generation=12,
        ),
    ),
]
OPERATOR_MUELSYSE = [
    api.Vanguard(
        name="Muelsyse P1",
        cost=15 - 4,  # talent Expenditure Economization E2
        skill=api.Skill(
            name="S1M3 - Progressive Moisturization",
            initial_sp=8,
            sp_cost=28,
            duration=15,
            total_dp_generation=13,
        ),
    ),
    api.Vanguard(
        name="Muelsyse P1",
        cost=15 - 4,  # talent Expenditure Economization E2
        skill=api.Skill(
            name="S2M3 - Ecological Interaction",
            initial_sp=18,
            sp_cost=35,
            duration=15,
            total_dp_generation=15,
        ),
    ),
    api.Vanguard(
        name="Muelsyse P1",
        cost=15 - 4,  # talent Expenditure Economization E2
        skill=api.Skill(
            name="S3M3 - Superficial Regulation",
            initial_sp=18,
            sp_cost=35,
            duration=15,
            total_dp_generation=15,
            instant=True,
        ),
    ),
]
OPERATOR_VIGIL = [
    api.Vanguard(
        name="Vigil P1",
        cost=15,
        skill=api.Skill(
            name="S1M3 - Packleader's Call",
            initial_sp=5,
            sp_cost=21,
            duration=0,
            total_dp_generation=7,
        ),
    ),
    api.Vanguard(
        name="Vigil P1",
        cost=15,
        skill=api.Skill(
            name="S2M3 - Packleader's Gift (no kills)",
            initial_sp=4,
            sp_cost=5,
            duration=0,
            total_dp_generation=2,  # 3 if he defeats an enemy
        ),
    ),
    api.Vanguard(
        name="Vigil P1",
        cost=15,
        skill=api.Skill(
            name="S3M3 - Packleader's Dignity",
            initial_sp=10,
            sp_cost=35,
            duration=15,
            total_dp_generation=12,
        ),
    ),
]
OPERATORS_TACTICIANS = [
    OPERATOR_BEANSTALK,
    OPERATOR_MUELSYSE,
    OPERATOR_VIGIL,
]

OPERATOR_CANTABILE = [
    api.Vanguard(
        name="Cantabile P6",
        cost=8,
        skill=api.Skill(
            name="S1M3 - Penetrating Gaze",
            initial_sp=9999,
            sp_cost=9999,
            duration=20,
            total_dp_generation=23,  # interval = 1s/(100+14+5); 20*interval=23.8
        ),
    ),
    api.Vanguard(
        name="Cantabile P6",
        cost=8,
        skill=api.Skill(
            name="S2M3 - Specular Reflection",
            initial_sp=20,
            sp_cost=25,
            duration=10.65,  # interval = 1s/(100+50+14+5); 18*interval=10.65
            total_dp_generation=18,
        ),
    ),
]
OPERATOR_PUZZLE = [
    api.Vanguard(
        name="Puzzle P6",
        cost=9,
        skill=api.Skill(
            name="S1M3 - Key Clue",
            initial_sp=2,
            sp_cost=5,
            duration=1,  # one attack
            total_dp_generation=3,
            instant=True,
        ),
        talent=api.DPTalent(
            name="Sequence E2",
            dp_to_trigger=0,
            dp_on_trigger=2,  # talent: attacks on full-hp enemies give +2 additional DP
            needs_to_be_deployed=True,
        ),
    ),
    # api.Vanguard(
    #     name="Puzzle P6",
    #     cost=9,
    #     skill=api.Skill(name="S1M3 - Key Clue (always full hp)",
    #         initial_sp=2,
    #         sp_cost=5,
    #         duration=1,# one attack
    #         total_dp_generation=3+12,
    #         instant=True,
    #     ),
    # ),
    api.Vanguard(
        name="Puzzle P6",
        cost=9,
        skill=api.Skill(
            name="S2M3 - Follow a Lead",
            initial_sp=14,
            sp_cost=26,
            duration=8,
            total_dp_generation=13,
        ),
        talent=api.DPTalent(
            name="Sequence E2",
            dp_to_trigger=0,
            dp_on_trigger=2,  # talent: attacks on full-hp enemies give +2 additional DP
            needs_to_be_deployed=True,
        ),
    ),
]
OPERATOR_INES = [
    api.Vanguard(
        name="Ines P1",
        cost=11,
        skill=api.Skill(
            name="S1M3 - Shadow Raid",
            initial_sp=2.78,  # interval = 1s/(100+8); 3*interval=2.78
            sp_cost=2.78,
            duration=0.93,  # one attack
            total_dp_generation=2,
            instant=True,
        ),
    ),
    api.Vanguard(
        name="Ines P1",
        cost=11,
        skill=api.Skill(
            name="S2M3 - Murky Night",
            initial_sp=15,
            sp_cost=20,
            duration=12,
            total_dp_generation=18,  # via testing
        ),
    ),
    api.Vanguard(
        name="Ines P1",
        cost=11,
        skill=api.Skill(
            name="S3M3 - Murky Night",
            initial_sp=9999,
            sp_cost=9999,
            duration=16,
            total_dp_generation=1 + 17,  # one enemy passed through by sentry
        ),
    ),
]
OPERATORS_AGENTS = [
    OPERATOR_CANTABILE,
    OPERATOR_PUZZLE,
    OPERATOR_INES,
]

OPERATORS = [
    *OPERATORS_FLAGBEARERS,
    *OPERATORS_PIONEERS,
    *OPERATORS_TACTICIANS,
    *OPERATORS_AGENTS,
]
ALL_OPERATOR_SKILLS = sum(
    OPERATORS, start=[]
)  # add up all the lists of operator skills into one big list
