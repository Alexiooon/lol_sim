"""Class defining Shen as a champion."""

from ._champion import BaseChampion


class Shen(BaseChampion):
    """Shen."""

    _str_cdragon = "shen"    # Name under DataDragon
    _str_ddragon = "shen"    # Name under CommunityDragon
    _str_data = "shen"       # Internal data name
    _str_printable = "Shen"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Shen._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Shen._str_printable
