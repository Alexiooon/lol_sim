"""Class defining Bel'Veth as a champion."""

from ._champion import BaseChampion


class BelVeth(BaseChampion):
    """Bel'Veth."""

    _str_cdragon = "belveth"    # Name under DataDragon
    _str_ddragon = "belveth"    # Name under CommunityDragon
    _str_data = "belveth"       # Internal data name
    _str_printable = "Bel'Veth"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return BelVeth._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return BelVeth._str_printable
