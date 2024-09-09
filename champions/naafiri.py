"""Class defining Naafiri as a champion."""

from ._champion import BaseChampion


class Naafiri(BaseChampion):
    """Naafiri."""

    _str_cdragon = "naafiri"    # Name under DataDragon
    _str_ddragon = "naafiri"    # Name under CommunityDragon
    _str_data = "naafiri"       # Internal data name
    _str_printable = "Naafiri"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Naafiri._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Naafiri._str_printable
