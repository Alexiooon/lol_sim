"""Module defining the event loop and valid events."""
from champion import BaseChampion


class EventLoop():
    """Event loop."""

    def __init__(self) -> None:
        """Init."""
        self._nodes = []
        self._current_time = 0

    def get_status(self, timestamp: int):
        """Calculate status of all nodes involved at a specific point in time."""

    def run(self):
        """Run through the entire event loop."""

    def next(self):
        """Handle next event."""


class EQSingleton():
    """Event queue, following the singleton pattern as to only allow a single instance."""

    class EQInstance():
        """The Event Queue instance."""

        def __init__(self) -> None:
            """Init."""
            self._champions = []  # All champions included in the simulation
            self._events = []

        def _sort(self):
            """Sort the event queue based on each events timestamp."""
            raise NotImplementedError

        def run(self):
            """Run through the entire event loop."""
            raise NotImplementedError

        def add_champion(self, champion: BaseChampion) -> None:
            """Add a champion to the event queue."""
            # Make sure the champion isn't already added.
            existing_champions = [str(champ) for champ in self._champions]
            if str(champion) in existing_champions:
                return
            self._champions.append(champion)

        def reset_all(self) -> None:
            """Clear the entire event queue and all participating champions."""
            self._champions = []
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
