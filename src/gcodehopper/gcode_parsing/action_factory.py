from typing import Any, Union
from gcodehopper.basemodel import BaseModel
import pydantic
from .comment_parser import CommentParser
from gcodehopper.enums.gcode_commands import GCodeCommands
from gcodehopper.encoded_representation.actions import (
    AbstractAction,
    MoveAction,
    SetBedTemperatureAction,
    SetToolTemperatureAction,
    SetExtrusionTypeAction,
    SetToolTemperatureAction,
    SetCoordinatesAction,
    SetToolPositionAction,
)

from .gcode_line import GCodeLine


class ActionFactory(BaseModel):

    def line_to_action(self, line: GCodeLine) -> Union[AbstractAction, None]:
        """Convert a line to an action."""

        action = self._action_mapping_dict.get(
            line.command, self._handle_unknown_command
        )(line)
        return action

    @property
    def _action_mapping_dict(self) -> dict[str, GCodeLine]:
        action_mapping_dict = {
            GCodeCommands.G0: self._create_move_action,
            GCodeCommands.G1: self._create_move_action,
            GCodeCommands.M82: self._create_extrude_settings_action,
            GCodeCommands.M83: self._create_extrude_settings_action,
            GCodeCommands.G92: self._create_move_action,
            GCodeCommands.M104: self._create_tool_temp_action,
            GCodeCommands.M106: self._create_fan_action,
            GCodeCommands.M107: self._create_fan_action,
            GCodeCommands.M109: self._create_tool_temp_action,
            GCodeCommands.M140: self._create_bed_temp_action,
            GCodeCommands.M190: self._create_bed_temp_action,
            # # TODO: Add more commands
        }
        return action_mapping_dict

    def _create_move_action(self, line: GCodeLine) -> AbstractAction:
        return MoveAction(
            x=line.X,
            y=line.Y,
            z=line.Z,
            e=line.E,
        )

    def _create_set_tool_position_action(self, line: GCodeLine) -> AbstractAction:
        return SetToolPositionAction(
            x=line.X,
            y=line.Y,
            z=line.Z,
            e=line.E,
            f=line.F,
        )

    def _create_extrude_settings_action(self, line: GCodeLine) -> AbstractAction:
        if line.command == GCodeCommands.M82:
            return SetExtrusionTypeAction(
                is_absolute=True,
            )
        elif line.command == GCodeCommands.M83:
            return SetExtrusionTypeAction(
                is_absolute=False,
            )
        else:
            raise ValueError(f"Unknown command {line.command}")

    def _create_bed_temp_action(self, line: GCodeLine) -> AbstractAction:
        return SetBedTemperatureAction(
            temperature=line.S,
        )

    def _create_tool_temp_action(self, line: GCodeLine) -> AbstractAction:
        return SetToolTemperatureAction(
            temperature=line.S,
        )

    def _create_fan_action(self, line: GCodeLine) -> AbstractAction:
        pass

    def _create_comment_action(self, line: GCodeLine) -> AbstractAction:
        pass

    def _create_coordinate_system_action(self, line: GCodeLine) -> AbstractAction:
        absolute_commands = [GCodeCommands.G90]
        relative_commands = [GCodeCommands.G91]

        if line.command in absolute_commands:
            return SetCoordinatesAction(
                is_absolute=True,
            )
        elif line.command in relative_commands:
            return SetCoordinatesAction(
                is_absolute=False,
            )
        else:
            raise ValueError(f"Unknown command {line.command}")

    def _handle_unknown_command(self, line: Any) -> AbstractAction:
        pass
