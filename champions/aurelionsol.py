"""Class defining Aurelion Sol as a champion."""

from ._champion import BaseChampion


class AurelionSol(BaseChampion):
    """Aurelion Sol."""

    _str_cdragon = "aurelionsol"    # Name under DataDragon
    _str_ddragon = "aurelionsol"    # Name under CommunityDragon
    _str_data = "aurelionsol"       # Internal data name
    _str_printable = "Aurelion Sol"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return AurelionSol._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return AurelionSol._str_printable
