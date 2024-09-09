"""Class defining Jayce as a champion."""

from ._champion import BaseChampion


class Jayce(BaseChampion):
    """Jayce."""

    _str_cdragon = "jayce"    # Name under DataDragon
    _str_ddragon = "jayce"    # Name under CommunityDragon
    _str_data = "jayce"       # Internal data name
    _str_printable = "Jayce"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Jayce._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Jayce._str_printable
