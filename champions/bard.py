"""Class defining Bard as a champion."""

from ._champion import BaseChampion


class Bard(BaseChampion):
    """Bard."""

    _str_cdragon = "bard"    # Name under DataDragon
    _str_ddragon = "bard"    # Name under CommunityDragon
    _str_data = "bard"       # Internal data name
    _str_printable = "Bard"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Bard._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Bard._str_printable
