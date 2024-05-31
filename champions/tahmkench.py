"""Class defining Tahm Kench as a champion."""

from ._champion import BaseChampion


class TahmKench(BaseChampion):
    """Tahm Kench."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Tahm Kench"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "tahmkench"

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return "Tahm Kench"
