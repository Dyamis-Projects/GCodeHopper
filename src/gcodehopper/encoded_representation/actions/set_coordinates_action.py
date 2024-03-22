from .abstract_action import AbstractAction
from gcodehopper.enums import ActionTypes, Coordinates
from gcodehopper.encoded_representation.representation_state import RepresentationState


class SetCoordinatesAction(AbstractAction):
    action_type: ActionTypes = ActionTypes.CHANGE_GLOBAL_SETTING
    is_absolute: bool

    def _apply_to_state(self, state: RepresentationState) -> RepresentationState:
        state = state.copy()
        if self.is_absolute:
            state.parameters.coordinates = Coordinates.ABSOLUTE
        else:
            state.parameters.coordinates = Coordinates.RELATIVE

        return state
