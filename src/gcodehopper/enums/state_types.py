from enum import Enum


class StateTypes(Enum):
    """Enum for the different types of states that can be observed by the agent."""

    UNKNOWN = "UNKNOWN"
    SOLID_INFILL = "SOLID_INFILL"
    WIPE = "WIPE"
    TRAVEL = "TRAVEL"
    SKIRT_BRIM = "SKIRT_BRIM"
