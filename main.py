#!/usr/bin/env python3
"""Main entry point for the League of Legends simulator."""

import argparse

import cli_main
import demo
import gui_main


def get_args() -> argparse.Namespace:
    """Get command line arguments."""
    args = argparse.ArgumentParser(description="Run the League of Legends simulator.")
    args.add_argument(
        "mode", type=str, choices=["cli", "gui", "demo"], default="gui",
        help="The mode to run the simulator in."
    )

    return args.parse_args()


def main():
    """Execute main functionality."""
    args = get_args()

    if args.mode == "cli":
        cli_main.run()

    elif args.mode == "gui":
        gui_main.run()

    elif args.mode == "demo":
        print("Running demo.")
        demo.demo()


if __name__ == "__main__":
    main()
