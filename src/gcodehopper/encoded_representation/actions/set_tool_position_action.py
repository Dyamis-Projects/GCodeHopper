from .abstract_action import AbstractAction
from gcodehopper.enums import ActionTypes, Coordinates
from gcodehopper.encoded_representation.representation_state import RepresentationState


class SetToolPositionAction(AbstractAction):
    action_type: ActionTypes = ActionTypes.MOVE
    x: float = None
    y: float = None
    z: float = None
    e: float = None
    f: float = None

    def _apply_to_state(self, state: RepresentationState) -> RepresentationState:

        state = state.copy()

        if self.x is not None:
            state.tool.x = self.x
        if self.y is not None:
            state.tool.y = self.y
        if self.z is not None:
            state.tool.z = self.z
        if self.e is not None:
            state.tool.e = self.e
        if self.f is not None:
            state.tool.f = self.f

        return state
