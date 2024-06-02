"""Module defining the different runes."""
# pylint: disable=too-few-public-methods
from typing import ClassVar


class RuneBaseClass():
    """Base class for common runepage methods."""

    by_name: ClassVar = {}
    by_index = tuple(by_name.values())

    def __getitem__(self, shard: int | str):
        """Return the stats from a shard."""
        if isinstance(shard, int):
            return self.by_index[shard]
        if isinstance(shard, str):
            return self.by_name[shard]
        raise TypeError("Rune shard must be either an integer or string.")


class OffenseShard(RuneBaseClass):
    """Defines the offensive shard choice in a rune page."""

    by_name: ClassVar = {
        "Adaptive Force": {"adaptiveForce": 9},
        "Attack Speed": {"attackSpeed": 10},
        "Ability Haste": {"abilityHaste": 8}
    }
    by_index = tuple(by_name.values())


class FlexShard(RuneBaseClass):
    """Defines the offensive shard choice in a rune page."""

    by_name: ClassVar = {
        "Adaptive Force": {"adaptiveForce": 9},
        "Move Speed": {"movementSpeed": 2},
        "Health Scaling": {"hpByLevel": tuple(10 * (i + 1) for i in range(10))}
    }
    by_index = tuple(by_name.values())


class DefenseShard(RuneBaseClass):
    """Defines the offensive shard choice in a rune page."""

    by_name: ClassVar = {
        "Health":  {"hp": 65},
        "Tenacity and Slow Resist": {"tenacity": 10, "slowResist": 10},
        "Health Scaling": {"hpByLevel": tuple(10 * (i + 1) for i in range(10))}
    }
    by_index = tuple(by_name.values())


offense = OffenseShard()
flex = FlexShard()
defense = DefenseShard()


# Small demo of functionality
if __name__ == "__main__":
    print("Rune shards can be selected either by name, or by index.")
    print('For example, "offense[0]" and "offense["Adaptive Force"]" will return the same value')
    print(f"offense[0] = {offense[0]}")
    print(f"offense['Adaptive Force'] = {offense['Adaptive Force']}")
