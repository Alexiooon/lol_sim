#!/usr/bin/env python3
"""Main interface for running simulator via CLI."""

import cmd

import champions
from event import EventQueue


class CommandHandler(cmd.Cmd):
    """Main loop for parsing and handling CLI commands."""

    # def __init__(
    #         self,
    #         completekey: str = "tab",
    #         stdin: cmd.IO[str] | None = None,
    #         stdout: cmd.IO[str] | None = None
    #     ) -> None:
    #     """Init."""
    #     super().__init__(completekey, stdin, stdout)

    #     self.__eventqueue = EventQueue()


    def do_add(self, champion: str) -> None:
        """Add a champion."""
        print(f"Adding {champion}.")
        EventQueue.add_champion(champion)

    def do_EOF(self, arg) -> bool:  # noqa: N802, PLR6301
        """Handle EOF."""
        return True

    def do_quit(self, arg) -> bool:  # noqa: PLR6301
        """Quit the program."""
        print("Quitting.")
        return True


def run():
    """Run main loop."""
    CommandHandler().cmdloop()


if __name__ == "__main__":
    run()
