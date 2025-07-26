import pydantic
import numpy as np


class Skill(pydantic.BaseModel):
    name: str

    initial_sp: float
    sp_cost: float
    duration: float
    total_dp_generation: int

    instant: bool = False
    sp_per_second: float = 1


class DPTalent(pydantic.BaseModel):
    name: str

    needs_to_be_deployed: bool = True
    dp_to_trigger: int
    dp_on_trigger: int


class DPRegenTalent(pydantic.BaseModel):
    name: str

    needs_to_be_deployed: bool = True
    dp_per_second: float


class Vanguard(pydantic.BaseModel):
    name: str
    cost: int

    skill: Skill
    talent: DPTalent | DPRegenTalent | None = None


class SimulationSetup(pydantic.BaseModel):
    name: str
    operator: Vanguard | None
    color: str | None = None

    time_step: float
    time_end: float

    dp_start: float = 0
    dp_per_second: float = 1


class SimulationResult(pydantic.BaseModel):
    name: str
    setup: SimulationSetup

    t: np.ndarray
    dp: np.ndarray

    class Config:
        arbitrary_types_allowed = True
