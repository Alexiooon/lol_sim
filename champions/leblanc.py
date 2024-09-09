"""Class defining LeBlanc as a champion."""

from ._champion import BaseChampion


class LeBlanc(BaseChampion):
    """LeBlanc."""

    _str_cdragon = "leblanc"    # Name under DataDragon
    _str_ddragon = "leblanc"    # Name under CommunityDragon
    _str_data = "leblanc"       # Internal data name
    _str_printable = "LeBlanc"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return LeBlanc._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return LeBlanc._str_printable
