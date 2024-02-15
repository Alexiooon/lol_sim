"""Define the different champions in the game and their stats."""


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

    def set_target(self, target: str):
        """Select a champion to autoattack."""
        self._target = target

    def _auto_attack(self, target: str | None = None):
        """Generate an auto attack."""
        # Ensure we are alive
        if not self.is_alive():
            return

        # Check for valid target
        if target is None:
            if self._target is None:
                raise ValueError("No valid target for autoattack.")
            target = self._target

        # Generate the damage event
        # TODO

    def _physical_damage_reduction(self) -> float:
        """Get the percentage damage reduction based on your armor."""
        return 100 / (100 + self.armor)

    def _auto_attack_hit(self, damage: float):
        """Take damage from an auto attack."""
        self.current_hitpoints -= damage * self._physical_damage_reduction()

    def is_alive(self) -> bool:
        """Check whether the champion is alive i.e. hitpoints is above (or equal) to zero."""
        return self.current_hitpoints >= 0


class KogMaw(BaseChampion):
    """Kog'Maw."""

    def __init__(self) -> None:
        """Init."""
        # Set the champions base stats
        # TODO: Instead of hard coding them here, load bin file from cdragon.
        self.ability_power = 0
        self.attack_damage = 61
        self.magic_resist = 30
        self.attack_speed = 0.665
        self.magic_resist = 30
        self.armor = 24
        self.hitpoints = 635
        super().__init__()


    def __str__(self) -> str:
        """String representation of champion."""
        return "Kog'Maw"
