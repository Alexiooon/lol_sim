"""Class defining Udyr as a champion."""

from ._champion import BaseChampion


class Udyr(BaseChampion):
    """Udyr."""

    _str_cdragon = "udyr"    # Name under DataDragon
    _str_ddragon = "udyr"    # Name under CommunityDragon
    _str_data = "udyr"       # Internal data name
    _str_printable = "Udyr"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Udyr._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Udyr._str_printable
