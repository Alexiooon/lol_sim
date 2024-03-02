#!/usr/bin/env python3
"""Base file for some testing."""

import champion
from event import EventQueue


def run_auto_attack_simulation():
    """Run a simulation of autoattacks until one person loses."""
    for _ in range(5):
        for champ in EventQueue.champions:
            event, delay = champ.get_next_attack()
            last_timestamp = EventQueue.get_last_timestamp(str(champ))
            EventQueue.add_event(event, last_timestamp + delay)
    EventQueue.print_queue()



def main():
    """Execute demo functionality."""
    # Create champion instances
    sivir = champion.Sivir()
    kog = champion.KogMaw()

    # Set their targets as each other
    sivir.set_target(str(kog))
    kog.set_target(str(sivir))

    # Add to event queue
    EventQueue.add_champion(sivir)
    EventQueue.add_champion(kog)

    run_auto_attack_simulation()

if __name__ == "__main__":
    main()
