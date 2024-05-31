"""Class defining Twisted Fate as a champion."""

from ._champion import BaseChampion


class TwistedFate(BaseChampion):
    """Twisted Fate."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Twisted Fate"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "twistedfate"

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return "Twisted Fate"
