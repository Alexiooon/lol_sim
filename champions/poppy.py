"""Class defining Poppy as a champion."""

from ._champion import BaseChampion


class Poppy(BaseChampion):
    """Poppy."""

    _str_cdragon = "poppy"    # Name under DataDragon
    _str_ddragon = "poppy"    # Name under CommunityDragon
    _str_data = "poppy"       # Internal data name
    _str_printable = "Poppy"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Poppy._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Poppy._str_printable
