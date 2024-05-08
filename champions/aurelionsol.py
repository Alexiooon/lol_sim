"""Class defining Aurelion Sol as a champion."""

from ._champion import BaseChampion


class AurelionSol(BaseChampion):
    """Aurelion Sol."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Aurelion Sol"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "aurelionsol"
