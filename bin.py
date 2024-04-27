"""Module for managing champion bin.json files."""

import json
import logging
import os

# Main directory containing bin data
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data_bin")

# Base stat names
BASE_STATS = [
    # HP
    "baseHP",
    "hpPerLevel",
    "baseStaticHPRegen",
    "hpRegenPerLevel",

    # Attack damage
    "baseDamage",
    "damagePerLevel",

    # Armor
    "baseArmor",
    "armorPerLevel",

    # Magic resist
    "baseSpellBlock",
    "spellBlockPerLevel",

    # Attack speed
    "attackSpeed",  # TODO: Handle (and write down) how the calculates
    "attackSpeedRatio",
    "attackSpeedPerLevel",

    # Misc
    "attackRange",
    "baseMoveSpeed",
    "acquisitionRange",  # TODO: Figure out what this is
]

# Ability resource (e.g. mana)
# Kept separate since its a nested dict in data file
AR_STATS = [
    "arType",  # TODO: 0 probably refers to mana, figure out the rest
    "arBase",
    "arPerLevel",
    "arBaseStaticRegen",
    "arRegenPerLevel",
]

# Champion string representations in bin.json
CHAMPION_STR_REP = {
    "kogmaw": "KogMaw",
    "sivir": "Sivir",
}


def _base_stat_key(champ: str) -> str:
    """Return the key which base stats are stored under in a champions bin.json file."""
    return "Characters/" + CHAMPION_STR_REP[champ] + "/CharacterRecords/Root"


def load_base_stats(champ: str):
    """Load the base stats of a champion and return as a dictionary."""
    # Load data if available under data_bin folder
    bin_file = os.path.join(DATA_DIR, champ + ".json")
    try:
        with open(bin_file, "r", encoding="utf8") as _file:
            data = dict(json.load(_file))[_base_stat_key(champ)]
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Data file is not available for '{champ}'") from exc

    # Extract the relevant data
    base_stats = {key: round(data[key], 3) for key in BASE_STATS}
    for key in AR_STATS:  # Ability resource handled separately
        try:  # Not sure how ability resource is handled for every champ, keep like this for now
            base_stats[key] = round(data[key, 3])
        except KeyError:
            pass

    return base_stats


if __name__ == "__main__":
    load_base_stats("sivir")
