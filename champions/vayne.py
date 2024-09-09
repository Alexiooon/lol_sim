"""Class defining Vayne as a champion."""

from ._champion import BaseChampion


class Vayne(BaseChampion):
    """Vayne."""

    _str_cdragon = "vayne"    # Name under DataDragon
    _str_ddragon = "vayne"    # Name under CommunityDragon
    _str_data = "vayne"       # Internal data name
    _str_printable = "Vayne"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Vayne._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Vayne._str_printable
