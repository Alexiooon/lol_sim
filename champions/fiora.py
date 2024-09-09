"""Class defining Fiora as a champion."""

from ._champion import BaseChampion


class Fiora(BaseChampion):
    """Fiora."""

    _str_cdragon = "fiora"    # Name under DataDragon
    _str_ddragon = "fiora"    # Name under CommunityDragon
    _str_data = "fiora"       # Internal data name
    _str_printable = "Fiora"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Fiora._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Fiora._str_printable
