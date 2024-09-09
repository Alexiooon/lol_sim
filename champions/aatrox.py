"""Class defining Aatrox as a champion."""

from ._champion import BaseChampion


class Aatrox(BaseChampion):
    """Aatrox."""

    _str_cdragon = "aatrox"    # Name under DataDragon
    _str_ddragon = "aatrox"    # Name under CommunityDragon
    _str_data = "aatrox"       # Internal data name
    _str_printable = "Aatrox"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Aatrox._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Aatrox._str_printable
