"""Class defining Sivir as a champion."""

from .champion import BaseChampion


class KogMaw(BaseChampion):
    """Kog'Maw."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Kog'Maw"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "kogmaw"
