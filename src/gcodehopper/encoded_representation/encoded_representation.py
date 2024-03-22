from gcodehopper.basemodel import BaseModel
from .representation_state import RepresentationState
from .state_updater import StateUpdater
from .actions.abstract_action import AbstractAction
import pydantic


class EncodedRepresentation(BaseModel):
    """Class for representing encoded gcode."""

    state: RepresentationState
    actions: list[AbstractAction]
    action_index: int = 0

    def next(self) -> RepresentationState:
        """Get to the next state."""

        self._log_trace(
            f"Getting next state from {self.state} with action {self.actions[self.action_index]}"
        )
        new_state = StateUpdater.update(
            state=self.state, action=self.actions[self.action_index]
        )

        new_class = EncodedRepresentation(
            state=new_state,
            actions=self.actions,
            action_index=self.action_index + 1,
        )

        return new_class

    """-------------------------------Pydantic Validation-------------------------------"""  # pylint: disable=W0105

    @classmethod
    @pydantic.validator("state")
    def validate_state(cls, v):  # pylint: disable=C0116
        assert isinstance(v, RepresentationState)
        return v

    @classmethod
    @pydantic.validator("actions")
    def validate_actions(cls, v):  # pylint: disable=C0116
        assert isinstance(v, list)
        for action in v:
            assert isinstance(action, AbstractAction)
        return v

    @classmethod
    @pydantic.validator("action_index")
    def validate_action_index(cls, v):  # pylint: disable=C0116
        assert isinstance(v, int)
        assert v >= 0
        return v
