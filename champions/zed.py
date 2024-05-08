"""Class defining Zed as a champion."""

from ._champion import BaseChampion


class Zed(BaseChampion):
    """Zed."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Zed"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "zed"
