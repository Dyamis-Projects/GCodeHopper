from gcodehopper.enums import Planes, Coordinates, Units
from gcodehopper.basemodel import BaseModel


class StateParameters(BaseModel):
    width: float = None
    bed_temperature: float = None
    units: Units = Units.UNKNOWN
    axes: Planes = Planes.UNKNOWN
    coordinates: Coordinates = Coordinates.UNKNOWN

    @classmethod
    def empty(cls) -> "StateParameters":
        cls._log_trace("Creating empty StateParameters")
        return cls()
