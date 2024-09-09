"""Shared code regarding champions stats and data."""

import os

# Main directory containing bin data
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data_bin"))

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
    "attackSpeed",
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
