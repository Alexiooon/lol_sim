"""Class defining Dr.Mundo as a champion."""

from ._champion import BaseChampion


class DrMundo(BaseChampion):
    """Dr.Mundo."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Dr.Mundo"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "drmundo"
