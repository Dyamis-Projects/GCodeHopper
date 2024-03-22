from .actions.abstract_action import AbstractAction
from .representation_state import RepresentationState


class StateUpdater:
    @classmethod
    def update(
        cls, state: RepresentationState, action: AbstractAction
    ) -> RepresentationState:
        return action.apply_to_state(state=state)
