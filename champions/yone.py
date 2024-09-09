"""Class defining Yone as a champion."""

from ._champion import BaseChampion


class Yone(BaseChampion):
    """Yone."""

    _str_cdragon = "yone"    # Name under DataDragon
    _str_ddragon = "yone"    # Name under CommunityDragon
    _str_data = "yone"       # Internal data name
    _str_printable = "Yone"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Yone._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Yone._str_printable
