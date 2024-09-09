"""Class defining Anivia as a champion."""

from ._champion import BaseChampion


class Anivia(BaseChampion):
    """Anivia."""

    _str_cdragon = "anivia"    # Name under DataDragon
    _str_ddragon = "anivia"    # Name under CommunityDragon
    _str_data = "anivia"       # Internal data name
    _str_printable = "Anivia"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Anivia._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Anivia._str_printable
