"""Module init."""
# Import all champions
from .champion import BaseChampion  # noqa: I001

from .kogmaw import KogMaw
from .sivir import Sivir

# List of all champions, as their base classes
CHAMPIONS: list[BaseChampion] = [
    Sivir,
    KogMaw,
]

# Data string representation of champion, typically in file names or accessing data.
CHAMPION_DATA_STR = [
    champ.data_str() for champ in CHAMPIONS
]
