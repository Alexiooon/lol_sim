"""Class defining Renata Glasc as a champion."""

from ._champion import BaseChampion


class RenataGlasc(BaseChampion):
    """Renata Glasc."""

    _str_cdragon = "renata"          # Name under DataDragon
    _str_ddragon = "renata"          # Name under CommunityDragon
    _str_data = "renataglasc"        # Internal data name
    _str_printable = "Renata Glasc"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return RenataGlasc._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return RenataGlasc._str_printable
