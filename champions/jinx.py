"""Class defining Jinx as a champion."""

from ._champion import BaseChampion


class Jinx(BaseChampion):
    """Jinx."""

    _str_cdragon = "jinx"    # Name under DataDragon
    _str_ddragon = "jinx"    # Name under CommunityDragon
    _str_data = "jinx"       # Internal data name
    _str_printable = "Jinx"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Jinx._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Jinx._str_printable
