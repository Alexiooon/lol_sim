"""Class defining Sett as a champion."""

from ._champion import BaseChampion


class Sett(BaseChampion):
    """Sett."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Sett"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "sett"
