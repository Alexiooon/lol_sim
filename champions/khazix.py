"""Class defining Kha'Zix as a champion."""

from ._champion import BaseChampion


class KhaZix(BaseChampion):
    """Kha'Zix."""

    _str_cdragon = "khazix"    # Name under DataDragon
    _str_ddragon = "khazix"    # Name under CommunityDragon
    _str_data = "khazix"       # Internal data name
    _str_printable = "Kha'Zix"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return KhaZix._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return KhaZix._str_printable
