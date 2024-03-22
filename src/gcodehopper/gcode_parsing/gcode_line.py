from typing import Any, Union
from gcodehopper.basemodel import BaseModel
import pydantic
from .comment_parser import CommentParser
from gcodehopper.enums.gcode_commands import GCodeCommands


class GCodeLine(BaseModel):
    args: list[str]  # list of arguments
    comment: str  # comment

    comment_parser: CommentParser = CommentParser()

    ARG_DELIMETER: str = " "
    COMMENT_DELIMETER: str = ";"
    LINE_FORMATTER: str = "{arg_string}" + f" {COMMENT_DELIMETER} " + "{comment}"

    PARAM_INDEX = 0

    @classmethod
    def from_string(cls, string: str) -> "GCodeLine":
        """Create a line object from a string (e.g. "G1 X10 Y10 F100 ; comment")

        Args:
            string (str): The string to parse, a line in a gcode file

        Returns:
            AbstractLine: The line object
        """
        args, comment = cls._string_to_args_and_comment(string=string)

        return cls(args=args, comment=comment)

    def to_string(self) -> str:
        """Convert the line object to a string (e.g. "G1 X10 Y10 F100 ; comment")

        Returns:
            str: The string representation of the line
        """
        arg_string = self.ARG_DELIMETER.join(self.args)
        return self.LINE_FORMATTER.format(arg_string=arg_string, comment=self.comment)

    # def to_dict(self) -> dict:
    #     var_dict = {
    #         "command": self.command,
    #         **{dim: self.get_value(dim) for dim in self.all_dimensions},
    #         "comment": self.comment_parser.parse(self.comment),
    #     }
    #     var_dict = {k: v for k, v in var_dict.items() if v is not None}
    #     return var_dict

    @classmethod
    def _string_to_args_and_comment(cls, string: str) -> tuple[list[str], str]:
        comment, args = string.split(cls.COMMENT_DELIMETER, 1)
        args = args.split(cls.ARG_DELIMETER)
        return args, comment

    @property
    def command(self) -> GCodeCommands:
        try:
            command = GCodeCommands(self.args[0])
        except ValueError:
            self._log_trace(f"Command {self.args[0]} not supported")
            command = GCodeCommands.UNSUPPORTED
        return command

    @classmethod
    def extract_param(cls, string: str) -> str:
        return string[cls.PARAM_INDEX]

    @classmethod
    def extract_value(cls, string: str) -> str:
        # FIXME: this does work, but id like a smarter way of doing this
        # in case of  non-single-letter parameters
        number_repr = string[cls.PARAM_INDEX : -1]

        # number repr will be a string
        # e.g. "10.236" or "-4.32" or ".232" or "10"
        # we want to convert it to a float
        number = float(number_repr)
        return number

    @property
    def non_command_args(self) -> list[str]:
        return self.args[1:]

    @property
    def params(self) -> list[str]:
        return [self.extract_param(arg) for arg in self.non_command_args]

    @property
    def values(self) -> list[float]:
        return [self.extract_value(arg) for arg in self.non_command_args]

    def get_value(self, param: str) -> Union[float, None]:
        # FIXME: This is not an ideal setup in terms of performance I believe.
        # something to look into if it becomes a bottleneck
        try:
            index = self.params.index(param)
            return self.values[index]
        except ValueError:
            self._log_trace(f"Parameter {param} not found in line {self}")
            return None

    """-------------------------------Properties-------------------------------"""

    @property
    def all_dimensions(self) -> list[str]:
        return ["X", "Y", "Z", "E", "F", "S"]

    @property
    def X(self) -> Union[float, None]:
        return self.get_value("X")

    @property
    def Y(self) -> Union[float, None]:
        return self.get_value("Y")

    @property
    def Z(self) -> Union[float, None]:
        return self.get_value("Z")

    @property
    def E(self) -> Union[float, None]:
        return self.get_value("E")

    @property
    def F(self) -> Union[float, None]:
        return self.get_value("F")

    def S(self) -> Union[float, None]:
        return self.get_value("S")

    @property
    def parsed_comment(self) -> dict:
        return self.comment_parser.parse(self.comment)

    """-------------------------------Pydantic Validation-------------------------------"""

    @classmethod
    @pydantic.validator("comment_parser")
    def validate_comment_parser(cls, v: Any) -> CommentParser:
        assert isinstance(v, CommentParser)
        return v
