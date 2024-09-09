"""Class defining Rek'Sai as a champion."""

from ._champion import BaseChampion


class RekSai(BaseChampion):
    """Rek'Sai."""

    _str_cdragon = "reksai"    # Name under DataDragon
    _str_ddragon = "reksai"    # Name under CommunityDragon
    _str_data = "reksai"       # Internal data name
    _str_printable = "Rek'Sai"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return RekSai._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return RekSai._str_printable
