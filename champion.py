"""Define the different champions in the game and their stats."""

from bin import load_base_stats


class BaseChampion():
    """Base class of a champion."""
    # pylint: disable=too-many-instance-attributes

    def __init__(self) -> None:
        """Init."""
        # Base stats
        self.attack_damage = 0.
        self.magic_resist = 0.
        self.ability_power = 0.
        self.attack_speed = 0.
        self.magic_resist = 0.
        self.armor = 0.
        self.hitpoints = 0.

        # Actual live stats
        # Currently only track hitpoints. In the future most stats should be
        # tracked due to various effects.
        self.current_hitpoints = self.hitpoints

        # Misc
        self._target = None  # Default target for auto attacks
        self._aa_cooldown = 0  # Seconds until the champion can auto attack again.

        # Load base stats available from cdragon.
        # TODO: Currently these are not used. I think the currently used attributes for stats
        # e.g. attack_damage should stay (or be grouped into a live_stats dict) since its affected
        # by items, levels, etc.
        self._base_stats = self._load()

    def __str__(self) -> str:
        """Pretty string representation of champion, typically for printing."""
        raise NotImplementedError("This should be defined in child class.")

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        raise NotImplementedError("This should be defined in child class.")

    def _load(self):
        """Load base stats for the champion."""
        return load_base_stats(self.data_str())

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
        self.current_hitpoints -= damage * self._physical_damage_reduction()
        print(f"{self} takes {damage:.0f} damage. New hitpoints: {self.current_hitpoints:.0f}")

    def is_alive(self) -> bool:
        """Check whether the champion is alive i.e. hitpoints is above (or equal) to zero."""
        return self.current_hitpoints >= 0


class KogMaw(BaseChampion):
    """Kog'Maw."""

    def __init__(self) -> None:
        """Init."""
        super().__init__()

        # Set the champions base stats
        # TODO: Instead of hardcoding them here, load bin file from cdragon.
        self.ability_power = 0
        self.attack_damage = 61
        self.magic_resist = 30
        self.attack_speed = 0.665
        self.armor = 24
        self.hitpoints = 635
        self.current_hitpoints = self.hitpoints

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Kog'Maw"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "kogmaw"


class Sivir(BaseChampion):
    """Sivir."""

    def __init__(self) -> None:
        """Init."""
        super().__init__()

        # Set the champions base stats
        # TODO: Instead of hard coding them here, load bin file from cdragon.
        self.ability_power = 0
        self.attack_damage = 58
        self.magic_resist = 30
        self.attack_speed = 0.625
        self.magic_resist = 30
        self.armor = 26
        self.hitpoints = 600
        self.current_hitpoints = self.hitpoints

    def __str__(self) -> str:
        """Pretty string representation of champion."""
        return "Sivir"

    @staticmethod
    def data_str() -> str:
        """Data string representation of champion, typically in file names or accessing data."""
        return "sivir"
