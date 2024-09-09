"""Class defining Swain as a champion."""

from ._champion import BaseChampion


class Swain(BaseChampion):
    """Swain."""

    _str_cdragon = "swain"    # Name under DataDragon
    _str_ddragon = "swain"    # Name under CommunityDragon
    _str_data = "swain"       # Internal data name
    _str_printable = "Swain"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Swain._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Swain._str_printable
