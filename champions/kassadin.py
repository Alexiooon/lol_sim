"""Class defining Kassadin as a champion."""

from ._champion import BaseChampion


class Kassadin(BaseChampion):
    """Kassadin."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Kassadin"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "kassadin"
