from .abstract_action import AbstractAction
from gcodehopper.enums import ActionTypes, ExtrusionTypes
from gcodehopper.encoded_representation.representation_state import RepresentationState


class SetExtrusionTypeAction(AbstractAction):
    action_type: ActionTypes = ActionTypes.CHANGE_TOOL_SETTING
    is_absolute: bool

    def _apply_to_state(self, state: RepresentationState) -> RepresentationState:
        state = state.copy()
        if self.is_absolute:
            state.tool.extrusion_type = ExtrusionTypes.ABSOLUTE
        else:
            state.tool.extrusion_type = ExtrusionTypes.RELATIVE

        return state
