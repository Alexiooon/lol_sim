"""Class defining Morgana as a champion."""

from ._champion import BaseChampion


class Morgana(BaseChampion):
    """Morgana."""

    _str_cdragon = "morgana"    # Name under DataDragon
    _str_ddragon = "morgana"    # Name under CommunityDragon
    _str_data = "morgana"       # Internal data name
    _str_printable = "Morgana"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Morgana._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Morgana._str_printable
