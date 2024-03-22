from .abstract_action import AbstractAction
from gcodehopper.enums import ActionTypes, Coordinates
from gcodehopper.encoded_representation.representation_state import RepresentationState


class MoveAction(AbstractAction):
    action_type: ActionTypes = ActionTypes.MOVE
    x: float
    y: float
    z: float = None
    e: float = None
    f: float = None

    def _apply_to_state(self, state: RepresentationState) -> RepresentationState:
        if state.parameters.coordinates == Coordinates.ABSOLUTE:
            return self._handle_apply_with_absolute_coordinates(state)
        elif state.parameters.coordinates == Coordinates.RELATIVE:
            return self._handle_apply_with_relative_coordinates(state)
        elif state.parameters.coordinates == Coordinates.UNKNOWN:
            return self._handle_apply_with_unknown_coordinates(state)
        else:
            raise ValueError(
                f"Cannot apply move action with unknown coordinates {state.parameters.coordinates}"
            )

    def _handle_apply_with_absolute_coordinates(
        self, state: RepresentationState
    ) -> RepresentationState:
        state = state.copy()
        state.tool.x = self.x
        state.tool.y = self.y

        if self.z is not None:
            state.tool.z = self.z

        if self.e is not None:
            state.tool.e = self.e

        return state

    def _handle_apply_with_relative_coordinates(
        self, state: RepresentationState
    ) -> RepresentationState:
        state = state.copy()
        state.tool.x += self.x
        state.tool.y += self.y

        if self.z is not None:
            state.tool.z += self.z

        if self.e is not None:  # FIXME: is this how this should work?
            state.tool.e += self.e

        return state

    def _handle_apply_with_unknown_coordinates(
        self, state: RepresentationState
    ) -> RepresentationState:
        raise ValueError("Cannot apply move action with unknown coordinates")
