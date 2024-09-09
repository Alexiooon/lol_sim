"""Class defining Qiyana as a champion."""

from ._champion import BaseChampion


class Qiyana(BaseChampion):
    """Qiyana."""

    _str_cdragon = "qiyana"    # Name under DataDragon
    _str_ddragon = "qiyana"    # Name under CommunityDragon
    _str_data = "qiyana"       # Internal data name
    _str_printable = "Qiyana"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Qiyana._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Qiyana._str_printable
