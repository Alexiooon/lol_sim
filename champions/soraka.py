"""Class defining Soraka as a champion."""

from ._champion import BaseChampion


class Soraka(BaseChampion):
    """Soraka."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Soraka"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "soraka"
