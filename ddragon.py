"""Module for accessing Riots DataDragon."""

import logging
import os
import shutil

import requests

BASE_PATH = "https://ddragon.leagueoflegends.com"
PATCH = "14.15.1"
LANGUAGE = "en_US"
ICON_DIR = os.path.join(os.path.dirname(__file__), "gui", "icon")
REQUEST_STATUS_OK = 200


def get_champion_names() -> list[str]:
    """Return a list of champion names for the purpose of accessing data."""
    url = "/".join([BASE_PATH, "cdn", PATCH, "data", LANGUAGE, "champion.json"])
    logging.critical("Trying to load champion info at %s", url)
    response = requests.get(url, stream=True, timeout=1)
    if response.status_code != REQUEST_STATUS_OK:
        logging.warning("Failed to load champion info, error code %s.", response.status_code)
        return []

    # Parse the JSON file and return each champions name
    data = response.json()["data"]
    return list(data.keys())


def get_square_icon(champ: str) -> None:
    """Download champion square icon and save it locally if it doesn't exist."""
    url = "/".join([BASE_PATH, "cdn", PATCH, "img", "champion", champ]) + ".png"
    local_path = os.path.join(ICON_DIR, champ) + ".png"
    if os.path.exists(local_path):
        logging.debug("File already exists at %s, skip", local_path)
        return

    # Send request for image
    logging.debug("Trying to download %s icon at %s", champ, url)
    response = requests.get(url, stream=True, timeout=1)
    if response.status_code != REQUEST_STATUS_OK:
        logging.warning("Failed to access image, error code %s", response.status_code)
        return

    # Save locally
    with open(local_path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    logging.debug("Saved image to %s", local_path)


def main():
    """Demo functionality of trying to ping the riot server."""
    for champ in get_champion_names():
        get_square_icon(champ=champ)


if __name__ == "__main__":
    main()
