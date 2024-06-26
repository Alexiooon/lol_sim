"""Class defining Bel'Veth as a champion."""

from ._champion import BaseChampion


class BelVeth(BaseChampion):
    """Bel'Veth."""

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Bel'Veth"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "belveth"

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return "Bel'Veth"
