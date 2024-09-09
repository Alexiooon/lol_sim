"""Class defining Tahm Kench as a champion."""

from ._champion import BaseChampion


class TahmKench(BaseChampion):
    """Tahm Kench."""

    _str_cdragon = "tahmkench"    # Name under DataDragon
    _str_ddragon = "tahmkench"    # Name under CommunityDragon
    _str_data = "tahmkench"       # Internal data name
    _str_printable = "Tahm Kench"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return TahmKench._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return TahmKench._str_printable
