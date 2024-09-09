"""Class defining Jarvan IV as a champion."""

from ._champion import BaseChampion


class JarvanIV(BaseChampion):
    """Jarvan IV."""

    _str_cdragon = "jarvaniv"    # Name under DataDragon
    _str_ddragon = "jarvaniv"    # Name under CommunityDragon
    _str_data = "jarvaniv"       # Internal data name
    _str_printable = "Jarvan IV"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return JarvanIV._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return JarvanIV._str_printable
