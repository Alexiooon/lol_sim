"""Module defining the event loop and valid events."""
from champions.champion import BaseChampion

# Dictionary of commands as keys and a prettier, human readable format as values
PRINTABLE = {
    "_auto_attack_hit": "Auto attack",
    "_damage_take": "Damage taken"
}


class EQSingleton():
    """Event queue, following the singleton pattern as to only allow a single instance."""

    class EQInstance():
        """The Event Queue instance."""

        def __init__(self) -> None:
            """Init."""
            self.champions = []  # All champions included in the simulation
            self._events = []

        def _sort(self):
            """Sort the event queue based on each events timestamp."""
            self._events.sort(key=lambda x: x[1])

        def add_champion(self, champion: BaseChampion) -> None:
            """Add a champion to the event queue."""
            # Make sure the champion isn't already added.
            existing_champions = [str(champ) for champ in self.champions]
            if str(champion) in existing_champions:
                return
            self.champions.append(champion)

        def add_event(self, event: dict, timestamp: int):
            """Add an event to the queue."""
            self._events.append((event, timestamp))
            self._sort()

        def _str_to_champion(self, champion_name: str):
            """Find and return champion instance from its name."""
            return next(champ for champ in self.champions if champion_name == str(champ))

        def get_last_timestamp(self, champion: str | None = None):
            """Get the last timestamp for a champion."""
            champ_timestamps = [ev[1] for ev in self._events if ev[0]["source"] == champion]
            if not champ_timestamps:
                return 0
            return champ_timestamps[-1]

        def run(self):
            """Run through the Event Queue and apply and all effects."""
            for i, event in enumerate(self._events):
                # Find the champion based on target string
                target = self._str_to_champion(event[0]["target"])

                # Run the event
                # TODO: Error handling if attribute was not found
                getattr(target, event[0]["effect"])(*event[0]["args"])

                # Check end conditions (Someone has died)
                if any(not champ.is_alive() for champ in self.champions):
                    last_event_index = i
                    break

            # Clear extra events
            if last_event_index < len(self._events):
                del self._events[last_event_index + 1:]

        def print_queue(self) -> None:
            """Print all events in a pretty format."""
            print("\n========== Event Queue ==========")
            for event in self._events:
                command, timestamp = event
                event_str = f"{timestamp:6.3f} | "
                event_str += f"{PRINTABLE[command['effect']]:12s} | "
                event_str += f"{command['source']:>10s} --> "
                event_str += f"{command['target']:<10s}"
                print(event_str)
            print("\n")

        def reset_all(self) -> None:
            """Clear the entire event queue and all participating champions."""
            self.champions = []
            self._events = []

        def reset_queue(self) -> None:
            """Clear the entire event queue, but keeps the participating champions."""
            self._events = []

    # Storage of the instance reference
    __instance = None

    def __init__(self):
        """Initialize singleton instance."""
        if EQSingleton.__instance is None:
            EQSingleton.__instance = EQSingleton.EQInstance()

        # Store instance reference as the only member in the handle
        self.__dict__["_EQSingleton__instance"] = EQSingleton.__instance

    def __getattr__(self, attr):
        """Delegate access to implementation."""
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """Delegate access to implementation."""
        return setattr(self.__instance, attr, value)

# Initialize the event queue as the


EventQueue = EQSingleton()
