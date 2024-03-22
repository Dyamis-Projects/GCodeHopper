from enum import Enum


class Planes(Enum):
    """Enum for the different types of planes that can be observed by the agent."""

    XY: str = "XY"
    YZ: str = "YZ"
    ZX: str = "ZX"
    UNKNOWN: str = "UNKNOWN"
