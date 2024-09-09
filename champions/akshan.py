"""Class defining Akshan as a champion."""

from ._champion import BaseChampion


class Akshan(BaseChampion):
    """Akshan."""

    _str_cdragon = "akshan"    # Name under DataDragon
    _str_ddragon = "akshan"    # Name under CommunityDragon
    _str_data = "akshan"       # Internal data name
    _str_printable = "Akshan"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Akshan._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Akshan._str_printable
