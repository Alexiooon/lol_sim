"""Class defining Ryze as a champion."""

from ._champion import BaseChampion


class Ryze(BaseChampion):
    """Ryze."""

    _str_cdragon = "ryze"    # Name under DataDragon
    _str_ddragon = "ryze"    # Name under CommunityDragon
    _str_data = "ryze"       # Internal data name
    _str_printable = "Ryze"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Ryze._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Ryze._str_printable
