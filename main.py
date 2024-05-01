#!/usr/bin/env python3
"""Base file for some testing."""

import champion
from event import EventQueue


def run_auto_attack_simulation():
    """Run a simulation of autoattacks until one person loses."""
    for _ in range(15):
        for champ in EventQueue.champions:
            event, delay = champ.get_next_attack()
            last_timestamp = EventQueue.get_last_timestamp(str(champ))
            EventQueue.add_event(event, last_timestamp + delay)
    EventQueue.print_queue()
    EventQueue.run()


def main():
    """Execute demo functionality."""
    # Create champion instances
    sivir = champion.Sivir(level=1)
    kog = champion.KogMaw(level=1)

    # Print some base stats
    for champ in (sivir, kog):
        print(f"\n===== {champ} =====")
        print(f"Level: {champ.level}")
        print(f"HP: {champ.hp}")
        print(f"Armor: {champ.armor}")
        print(f"MR: {champ.magic_resist}")
        print(f"AD: {champ.attack_damage}")
        print(f"AS: {champ.attack_speed}")

    # Set their targets as each other
    sivir.set_target(str(kog))
    kog.set_target(str(sivir))

    # Add to event queue
    EventQueue.add_champion(sivir)
    EventQueue.add_champion(kog)

    run_auto_attack_simulation()


if __name__ == "__main__":
    main()
