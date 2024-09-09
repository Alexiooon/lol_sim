"""Class defining Evelynn as a champion."""

from ._champion import BaseChampion


class Evelynn(BaseChampion):
    """Evelynn."""

    _str_cdragon = "evelynn"    # Name under DataDragon
    _str_ddragon = "evelynn"    # Name under CommunityDragon
    _str_data = "evelynn"       # Internal data name
    _str_printable = "Evelynn"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Evelynn._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Evelynn._str_printable
