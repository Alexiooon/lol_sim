"""Class defining Vi as a champion."""

from ._champion import BaseChampion


class Vi(BaseChampion):
    """Vi."""

    _str_cdragon = "vi"    # Name under DataDragon
    _str_ddragon = "vi"    # Name under CommunityDragon
    _str_data = "vi"       # Internal data name
    _str_printable = "Vi"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Vi._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Vi._str_printable
