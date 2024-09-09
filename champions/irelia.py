"""Class defining Irelia as a champion."""

from ._champion import BaseChampion


class Irelia(BaseChampion):
    """Irelia."""

    _str_cdragon = "irelia"    # Name under DataDragon
    _str_ddragon = "irelia"    # Name under CommunityDragon
    _str_data = "irelia"       # Internal data name
    _str_printable = "Irelia"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Irelia._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Irelia._str_printable
