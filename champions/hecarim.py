"""Class defining Hecarim as a champion."""

from ._champion import BaseChampion


class Hecarim(BaseChampion):
    """Hecarim."""

    _str_cdragon = "hecarim"    # Name under DataDragon
    _str_ddragon = "hecarim"    # Name under CommunityDragon
    _str_data = "hecarim"       # Internal data name
    _str_printable = "Hecarim"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Hecarim._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Hecarim._str_printable
