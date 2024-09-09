"""Class defining Lux as a champion."""

from ._champion import BaseChampion


class Lux(BaseChampion):
    """Lux."""

    _str_cdragon = "lux"    # Name under DataDragon
    _str_ddragon = "lux"    # Name under CommunityDragon
    _str_data = "lux"       # Internal data name
    _str_printable = "Lux"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Lux._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Lux._str_printable
