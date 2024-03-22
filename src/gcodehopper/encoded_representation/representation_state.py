from gcodehopper.enums import StateTypes
from .state_parameters import StateParameters
from .tool_parameters import ToolParameters
from gcodehopper.basemodel import BaseModel
import pydantic


class RepresentationState(BaseModel):
    state_type: StateTypes = StateTypes.UNKNOWN
    parameters: StateParameters = StateParameters.empty()
    tool: ToolParameters = ToolParameters.empty()

    @classmethod
    @pydantic.validator("parameters")
    def validate_state_type(cls, v):  # pylint: disable=C0116
        assert isinstance(v, StateParameters)
        return v

    @classmethod
    @pydantic.validator("tool")
    def validate_tool_parameters(cls, v):  # pylint: disable=C0116
        assert isinstance(v, ToolParameters)
        return v

    def __repr__(self):
        return f"<{self.__class__.__name__}({self.state_type} {self.parameters} {self.tool})>"
