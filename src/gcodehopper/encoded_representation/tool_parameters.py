from gcodehopper.basemodel import BaseModel
from gcodehopper.enums import ExtrusionTypes


class ToolParameters(BaseModel):
    """
    Represents the parameters of a tool.

    Attributes:
        x: The x coordinate of the tool.
        y: The y coordinate of the tool.
        z: The z coordinate of the tool.
        e: The extrusion rate of the tool.
        f: The feed rate of the tool.
    """

    x: float = None
    y: float = None
    z: float = None
    e: float = None
    f: float = None
    temperature: float = None
    extrusion_type: ExtrusionTypes = ExtrusionTypes.UNKNOWN

    @classmethod
    def empty(cls) -> "ToolParameters":
        """
        Creates an empty instance of ToolParameters.
        """
        return cls()
