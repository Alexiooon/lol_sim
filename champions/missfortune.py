"""Class defining Miss Fortune as a champion."""

from ._champion import BaseChampion


class MissFortune(BaseChampion):
    """Miss Fortune."""

    _str_cdragon = "missfortune"    # Name under DataDragon
    _str_ddragon = "missfortune"    # Name under CommunityDragon
    _str_data = "missfortune"       # Internal data name
    _str_printable = "Miss Fortune"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return MissFortune._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return MissFortune._str_printable
