"""Class defining Maokai as a champion."""

from ._champion import BaseChampion


class Maokai(BaseChampion):
    """Maokai."""

    _str_cdragon = "maokai"    # Name under DataDragon
    _str_ddragon = "maokai"    # Name under CommunityDragon
    _str_data = "maokai"       # Internal data name
    _str_printable = "Maokai"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Maokai._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Maokai._str_printable
