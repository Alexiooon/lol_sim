"""Class defining Karma as a champion."""

from ._champion import BaseChampion


class Karma(BaseChampion):
    """Karma."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Karma"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "karma"
