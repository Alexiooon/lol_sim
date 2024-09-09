"""Class defining Hwei as a champion."""

from ._champion import BaseChampion


class Hwei(BaseChampion):
    """Hwei."""

    _str_cdragon = "hwei"    # Name under DataDragon
    _str_ddragon = "hwei"    # Name under CommunityDragon
    _str_data = "hwei"       # Internal data name
    _str_printable = "Hwei"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Hwei._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Hwei._str_printable
