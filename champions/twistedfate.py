"""Class defining Twisted Fate as a champion."""

from ._champion import BaseChampion


class TwistedFate(BaseChampion):
    """Twisted Fate."""

    _str_cdragon = "twistedfate"    # Name under DataDragon
    _str_ddragon = "twistedfate"    # Name under CommunityDragon
    _str_data = "twistedfate"       # Internal data name
    _str_printable = "Twisted Fate"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return TwistedFate._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return TwistedFate._str_printable
