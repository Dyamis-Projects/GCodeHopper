from enum import Enum


class ActionTypes(Enum):
    """Enum for the different types of actions that can be taken by the agent."""

    MOVE: str = "MOVE"
    CHANGE_GLOBAL_SETTING: str = "CHANGE_GLOBAL_SETTING"
    CHANGE_TOOL_SETTING: str = "CHANGE_TOOL_SETTING"
