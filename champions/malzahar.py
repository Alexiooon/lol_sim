"""Class defining Malzahar as a champion."""

from ._champion import BaseChampion


class Malzahar(BaseChampion):
    """Malzahar."""

    _str_cdragon = "malzahar"    # Name under DataDragon
    _str_ddragon = "malzahar"    # Name under CommunityDragon
    _str_data = "malzahar"       # Internal data name
    _str_printable = "Malzahar"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Malzahar._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Malzahar._str_printable
