from gcodehopper.basemodel import BaseModel
from gcodehopper.enums import ActionTypes
from gcodehopper.encoded_representation.representation_state import RepresentationState

from abc import ABC, abstractmethod


class AbstractAction(BaseModel, ABC):
    action_type: ActionTypes

    def apply_to_state(self, state: RepresentationState) -> RepresentationState:
        """Apply the action to the state."""
        self._log_trace(f"Applying {self} to {state}")
        return self._apply_to_state(state=state)

    @abstractmethod
    def _apply_to_state(self, state: RepresentationState) -> RepresentationState:
        raise NotImplementedError()

    def __repr__(self):
        return (
            f"<{self.__class__.__name__}(l-{self.layer_id} a-{self.action_id}) -"
            f"- ({self.action_type})>"
        )
