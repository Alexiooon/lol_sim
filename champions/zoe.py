"""Class defining Zoe as a champion."""

from ._champion import BaseChampion


class Zoe(BaseChampion):
    """Zoe."""

    _str_cdragon = "zoe"    # Name under DataDragon
    _str_ddragon = "zoe"    # Name under CommunityDragon
    _str_data = "zoe"       # Internal data name
    _str_printable = "Zoe"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Zoe._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Zoe._str_printable
