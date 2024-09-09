"""Class defining Shyvana as a champion."""

from ._champion import BaseChampion


class Shyvana(BaseChampion):
    """Shyvana."""

    _str_cdragon = "shyvana"    # Name under DataDragon
    _str_ddragon = "shyvana"    # Name under CommunityDragon
    _str_data = "shyvana"       # Internal data name
    _str_printable = "Shyvana"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Shyvana._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Shyvana._str_printable
