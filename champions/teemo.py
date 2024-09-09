"""Class defining Teemo as a champion."""

from ._champion import BaseChampion


class Teemo(BaseChampion):
    """Teemo."""

    _str_cdragon = "teemo"    # Name under DataDragon
    _str_ddragon = "teemo"    # Name under CommunityDragon
    _str_data = "teemo"       # Internal data name
    _str_printable = "Teemo"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return Teemo._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return Teemo._str_printable
