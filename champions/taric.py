"""Class defining Taric as a champion."""

from ._champion import BaseChampion


class Taric(BaseChampion):
    """Taric."""

    _str_cdragon = "taric"    # Name under DataDragon
    _str_ddragon = "taric"    # Name under CommunityDragon
    _str_data = "taric"       # Internal data name
    _str_printable = "Taric"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Taric._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Taric._str_printable
