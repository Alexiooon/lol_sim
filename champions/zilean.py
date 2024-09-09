"""Class defining Zilean as a champion."""

from ._champion import BaseChampion


class Zilean(BaseChampion):
    """Zilean."""

    _str_cdragon = "zilean"    # Name under DataDragon
    _str_ddragon = "zilean"    # Name under CommunityDragon
    _str_data = "zilean"       # Internal data name
    _str_printable = "Zilean"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Zilean._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Zilean._str_printable
