"""Class defining Xayah as a champion."""

from ._champion import BaseChampion


class Xayah(BaseChampion):
    """Xayah."""

    _str_cdragon = "xayah"    # Name under DataDragon
    _str_ddragon = "xayah"    # Name under CommunityDragon
    _str_data = "xayah"       # Internal data name
    _str_printable = "Xayah"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Xayah._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Xayah._str_printable
