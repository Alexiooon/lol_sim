"""Class defining Singed as a champion."""

from ._champion import BaseChampion


class Singed(BaseChampion):
    """Singed."""

    _str_cdragon = "singed"    # Name under DataDragon
    _str_ddragon = "singed"    # Name under CommunityDragon
    _str_data = "singed"       # Internal data name
    _str_printable = "Singed"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Singed._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Singed._str_printable
