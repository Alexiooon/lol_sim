"""Class defining K'Sante as a champion."""

from ._champion import BaseChampion


class KSante(BaseChampion):
    """K'Sante."""

    _str_cdragon = "ksante"    # Name under DataDragon
    _str_ddragon = "ksante"    # Name under CommunityDragon
    _str_data = "ksante"       # Internal data name
    _str_printable = "K'Sante"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return KSante._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return KSante._str_printable
