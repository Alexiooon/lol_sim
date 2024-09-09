"""Class defining Dr.Mundo as a champion."""

from ._champion import BaseChampion


class DrMundo(BaseChampion):
    """Dr.Mundo."""

    _str_cdragon = "drmundo"    # Name under DataDragon
    _str_ddragon = "drmundo"    # Name under CommunityDragon
    _str_data = "drmundo"       # Internal data name
    _str_printable = "Dr.Mundo"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return DrMundo._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return DrMundo._str_printable
