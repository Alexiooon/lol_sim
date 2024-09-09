"""Class defining Vex as a champion."""

from ._champion import BaseChampion


class Vex(BaseChampion):
    """Vex."""

    _str_cdragon = "vex"    # Name under DataDragon
    _str_ddragon = "vex"    # Name under CommunityDragon
    _str_data = "vex"       # Internal data name
    _str_printable = "Vex"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Vex._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Vex._str_printable
