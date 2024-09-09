"""Class defining Brand as a champion."""

from ._champion import BaseChampion


class Brand(BaseChampion):
    """Brand."""

    _str_cdragon = "brand"    # Name under DataDragon
    _str_ddragon = "brand"    # Name under CommunityDragon
    _str_data = "brand"       # Internal data name
    _str_printable = "Brand"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Brand._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Brand._str_printable
