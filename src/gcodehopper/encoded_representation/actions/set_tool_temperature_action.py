from .abstract_action import AbstractAction
from gcodehopper.enums import ActionTypes
from gcodehopper.encoded_representation.representation_state import RepresentationState


class SetToolTemperatureAction(AbstractAction):
    action_type: ActionTypes = ActionTypes.CHANGE_TOOL_SETTING
    temperature: float

    def _apply_to_state(self, state: RepresentationState) -> RepresentationState:
        state = state.copy()
        state.tool.temperature = self.temperature
        return state
