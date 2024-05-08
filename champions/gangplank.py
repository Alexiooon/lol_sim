"""Class defining Gangplank as a champion."""

from ._champion import BaseChampion


class Gangplank(BaseChampion):
    """Gangplank."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Gangplank"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "gangplank"
