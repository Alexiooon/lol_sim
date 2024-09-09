"""Define the different champions in the game and their stats."""

from bin import load_base_stats


class BaseChampion():
    """Base class of a champion."""
    # pylint: disable=too-many-instance-attributes

    _str_cdragon = ""   # Name under DataDragon
    _str_ddragon = ""   # Name under CommunityDragon
    str_data = ""       # Internal data name
    str_printable = ""  # Name in pretty "printable" format

    def __init__(self, level: int = 1) -> None:
        """Init."""
        # Live stats i.e. the stats which are actively used for calculations.
        # Note that currenlty the only sources are base stats + levels
        self.ability_power = 0.
        self.attack_damage = 0.
        self.attack_speed = 0.
        self.armor = 0.
        self.magic_resist = 0.
        self.hp = 0.
        self.max_hp = self.hp

        # Non-combat related stats
        self._level = level

        # Misc
        self._target = None  # Default target for auto attacks
        self._aa_cooldown = 0  # Seconds until the champion can auto attack again.

        # Load stats from cdragon
        self._base_stats = self._load()
        self.calc_stats()

    def __str__(self) -> str:
        """Pretty string representation of champion, typically for printing."""
        raise NotImplementedError("This should be defined in child class.")

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        raise NotImplementedError("This should be defined in child class.")

    @staticmethod
    def printable() -> str:
        """Pretty string representation of champion, typically for menus or as display name."""
        raise NotImplementedError("This should be defined in child class.")

    @property
    def level(self):
        """Level of the champion."""
        return self._level

    @level.setter
    def level(self, new_level: int):
        """Update champion stats when level changes."""
        self._level = new_level
        self.calc_stats()

    def _load(self):
        """Load base stats for the champion."""
        return load_base_stats(self.data_str())

    def calc_stats(self):
        """Calculate live stats from base and level.

        Note that this currently does not support any stats gained from runes or items.
        Reference: https://leagueoflegends.fandom.com/wiki/Champion_statistic#Increasing_Statistics
        """
        self.attack_damage = \
            self._base_stats["baseDamage"] + \
            self._base_stats["damagePerLevel"] * (self.level - 1) * \
            (0.7025 + 0.0175 * (self.level - 1))

        bonus_attack_speed = \
            self._base_stats["attackSpeedPerLevel"] * (self.level - 1) * \
            (0.7025 + 0.0175 * (self.level - 1))
        self.attack_speed = \
            self._base_stats["attackSpeed"] + \
            self._base_stats["attackSpeedRatio"] * (bonus_attack_speed / 100)

        self.max_hp = \
            self._base_stats["baseHP"] + \
            self._base_stats["hpPerLevel"] * (self.level - 1) * \
            (0.7025 + 0.0175 * (self.level - 1))
        self.hp = self.max_hp

        self.armor = \
            self._base_stats["baseArmor"] + \
            self._base_stats["armorPerLevel"] * (self.level - 1) * \
            (0.7025 + 0.0175 * (self.level - 1))

        self.magic_resist = \
            self._base_stats["baseSpellBlock"] + \
            self._base_stats["spellBlockPerLevel"] * (self.level - 1) * \
            (0.7025 + 0.0175 * (self.level - 1))

    # ========== Combat ==========
    def set_target(self, target: str):
        """Select a champion to autoattack."""
        self._target = target

    def auto_attack(self, target: str | None = None):
        """Generate an auto attack."""
        # Check for valid target
        if target is None:
            if self._target is None:
                raise ValueError("No valid target for autoattack.")
            target = self._target

        # Generate the damage event
        time_since_last_event = self._aa_cooldown
        self._aa_cooldown = self.attack_speed**-1
        aa_event = {
            "target": target,
            "source": str(self),
            "effect": "_auto_attack_hit",
            "args": (self.attack_damage,)
        }
        return aa_event, time_since_last_event

    def get_next_attack(self) -> tuple[dict, float]:
        """Get the next attack from this champion.

        Currently only auto attacks are implemented, without any special modifiers.
        """
        return self.auto_attack()

    def _physical_damage_reduction(self) -> float:
        """Get the percentage damage reduction based on your armor."""
        return 100 / (100 + self.armor)

    def _auto_attack_hit(self, damage: float) -> None:
        """Take damage from an auto attack."""
        self.max_hp -= damage * self._physical_damage_reduction()
        print(f"{self} takes {damage:.0f} damage. New hitpoints: {self.max_hp:.0f}")

    def is_alive(self) -> bool:
        """Check whether the champion is alive i.e. hitpoints is above (or equal) to zero."""
        return self.max_hp >= 0
