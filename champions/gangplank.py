"""Class defining Gangplank as a champion."""

from ._champion import BaseChampion


class Gangplank(BaseChampion):
    """Gangplank."""

    _str_cdragon = "gangplank"    # Name under DataDragon
    _str_ddragon = "gangplank"    # Name under CommunityDragon
    _str_data = "gangplank"       # Internal data name
    _str_printable = "Gangplank"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Gangplank._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Gangplank._str_printable
