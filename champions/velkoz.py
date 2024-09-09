"""Class defining Vel'Koz as a champion."""

from ._champion import BaseChampion


class VelKoz(BaseChampion):
    """Vel'Koz."""

    _str_cdragon = "velkoz"    # Name under DataDragon
    _str_ddragon = "velkoz"    # Name under CommunityDragon
    _str_data = "velkoz"       # Internal data name
    _str_printable = "Vel'Koz"  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        super().__init__(level=level)

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return self.printable()

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return VelKoz._str_data

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        return VelKoz._str_printable
