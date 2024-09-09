"""Class defining Master Yi as a champion."""

from ._champion import BaseChampion


class MasterYi(BaseChampion):
    """Master Yi."""

    _str_cdragon = "masteryi"    # Name under DataDragon
    _str_ddragon = "masteryi"    # Name under CommunityDragon
    _str_data = "masteryi"       # Internal data name
    _str_printable = "Master Yi"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return MasterYi._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return MasterYi._str_printable
