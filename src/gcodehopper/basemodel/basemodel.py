import pydantic
import yaml
import logging
import os
from gcodehopper.enums.log_levels import LogLevels
from typing import Union, Iterable


class BaseModel(pydantic.BaseModel):  # pylint: disable = E1101
    """
    Shared base model for all models in the project.
    """

    class Config:
        log_trace = True  # adding this to reduce potential slow down from logging

        pass
        # orm_mode = True
        # anystr_strip_whitespace = True
        # validate_assignment = True
        # use_enum_values = True
        # extra = "forbid"

    """-------------------------------Logging-------------------------------"""  # pylint: disable=W0105

    @classmethod
    def _log(cls, msg: Union[str, Iterable[str]], level: int = LogLevels.DEBUG):
        if not isinstance(msg, str):
            try:
                msg = "\n".join(msg)
            except TypeError:
                msg = str(msg)

        logging.log(level, msg)

    @classmethod
    def _log_trace(cls, msg: Union[str, Iterable[str]]):
        if not cls.Config.log_trace:
            return
        cls._log(msg, level=LogLevels.TRACE)

    @classmethod
    def _log_debug(cls, msg: Union[str, Iterable[str]]):
        cls._log(msg, level=LogLevels.DEBUG)

    @classmethod
    def _log_info(cls, msg: Union[str, Iterable[str]]):
        cls._log(msg, level=LogLevels.INFO)

    @classmethod
    def _log_warning(cls, msg: Union[str, Iterable[str]]):
        cls._log(msg, level=LogLevels.WARNING)

    @classmethod
    def _log_error(cls, msg: Union[str, Iterable[str]]):
        cls._log(msg, level=LogLevels.ERROR)

    @classmethod
    def _log_critical(cls, msg: Union[str, Iterable[str]]):
        cls._log(msg, level=LogLevels.CRITICAL)

    """-------------------------------Save/Load-------------------------------"""  # pylint: disable=W0105

    @classmethod
    def from_yaml(cls, file_path: os.PathLike) -> "BaseModel":
        """Load from yaml file."""
        cls._log_trace(f"Loading {cls.__name__} from {file_path}")
        loaded_dict = yaml.load(file_path, Loader=yaml.FullLoader)
        cls._log_trace(f"Loaded {cls.__name__} from {file_path}")
        return cls(**loaded_dict)

    def to_yaml(self, file_path: os.PathLike) -> bool:
        """Save to yaml file."""
        self._log_trace(f"Saving {self.__class__.__name__} to {file_path}")
        with open(file_path, "w") as file:
            yaml.dump(
                self.dict(), file, default_flow_style=False, sort_keys=False, indent=4
            )

        self._log_trace(f"Saved {self.__class__.__name__} to {file_path}")

        return True
