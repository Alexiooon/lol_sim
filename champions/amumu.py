"""Class defining Amumu as a champion."""

from ._champion import BaseChampion


class Amumu(BaseChampion):
    """Amumu."""

    _str_cdragon = "amumu"    # Name under DataDragon
    _str_ddragon = "amumu"    # Name under CommunityDragon
    _str_data = "amumu"       # Internal data name
    _str_printable = "Amumu"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Amumu._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Amumu._str_printable
