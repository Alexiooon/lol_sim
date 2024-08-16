"""Class defining Renata Glasc as a champion."""

from ._champion import BaseChampion


class RenataGlasc(BaseChampion):
    """Renata Glasc."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Renata Glasc"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "renata"

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return "Renata Glasc"
