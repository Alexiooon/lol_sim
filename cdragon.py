"""Common functions for getting data from Community Dragon (CD)."""

import json
import logging
import os

import requests

from champions import CHAMPION_DATA_STR

BASE_PATH = ("https://raw.communitydragon.org/"
             "latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/")
BIN_PATH = "https://raw.communitydragon.org/latest/game/data/characters"
STATUS_OK = 200

CHAMPION_TO_ID = {  # Champion IDs in Community Dragon
    "Ahri": "103",
    "Annie": "1",
    "Kayle": "10",
    "Shyvana": "102",
    "Xerath": "101",
}
ID_TO_CHAMPION = {value: key for key, value in CHAMPION_TO_ID.items()}


def update_constant_data() -> None:
    """Fetch relevant data from CD and save locally."""
    for champ, _id in CHAMPION_TO_ID.items():
        print("/".join([BASE_PATH, _id + ".json"]))
        data = requests.get(BASE_PATH + _id + ".json", timeout=100).json()
        del data["skins"]  # A lot of unnecessary data we're not interested in
        with open("./data/" + champ + ".json", "w", encoding="utf8") as _file:
            json.dump(data, _file, indent=2)


def get_champion(champ: str) -> None:
    """Get a specific champions data."""
    path = "/".join([BIN_PATH, champ, champ]) + ".bin.json"
    res = requests.get(path, timeout=100)
    if res.status_code != STATUS_OK:
        logging.warning("Failed to load champion data from %s", path)
    data = res.json()
    with open("./data_bin/" + champ + ".json", "w", encoding="utf8") as _file:
        json.dump(data, _file, indent=2)


def get_all_champions() -> None:
    """Download all champion bin.json data files from CommunityDragon."""
    local_path = os.path.join(os.path.dirname(__file__), "data_bin")
    for champ in CHAMPION_DATA_STR:
        if os.path.exists(os.path.join(local_path, champ + ".json")):
            logging.debug("Data for champion '%s' already exists, skip")
            continue
        get_champion(champ)


def main():
    """Execute demo functionality."""
    get_all_champions()


if __name__ == "__main__":
    main()
