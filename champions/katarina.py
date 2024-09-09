"""Class defining Katarina as a champion."""

from ._champion import BaseChampion


class Katarina(BaseChampion):
    """Katarina."""

    _str_cdragon = "katarina"    # Name under DataDragon
    _str_ddragon = "katarina"    # Name under CommunityDragon
    _str_data = "katarina"       # Internal data name
    _str_printable = "Katarina"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Katarina._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Katarina._str_printable
