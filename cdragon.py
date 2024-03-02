"""Common functions for getting data from Community Dragon (CD)."""

import json

import requests

BASE_PATH = ("https://raw.communitydragon.org/"
             "latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/")
BIN_PATH = "https://raw.communitydragon.org/latest/game/data/characters"
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
    data = requests.get(path, timeout=100).json()
    with open("./data_bin/" + champ + ".json", "w", encoding="utf8") as _file:
        json.dump(data, _file, indent=2)


def main():
    """Execute demo functionality."""
    # data = requests.get("", timeout=100).json()
    update_constant_data()
    get_champion("aatrox")


if __name__ == "__main__":
    main()
