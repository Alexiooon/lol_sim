"""Test suite for _common.py."""
# pylint: disable=protected-access
import os
import unittest

from champions import CHAMPIONS


class TestBaseChampion(unittest.TestCase):
    """Test suite for validating common champion methods and attributes."""

    def test_data_string(self):
        """Validate that '_str_data' attribute matches Python file name for the champion."""
        for champ in CHAMPIONS:
            filename = os.path.join("champions", champ.data_str() + ".py")
            self.assertTrue(
                os.path.isfile(filename),
                f"Champion {champ.printable()} has incorrect data str '{champ.data_str()}'"
            )

    def test_cdragon_string(self):
        """Validate that '_str_cdragon' attribute matches bin.json file name for the champion."""
        for champ in CHAMPIONS:
            filename = os.path.join("data_bin", champ._str_cdragon + ".json")
            self.assertTrue(
                os.path.isfile(filename),
                f"Champion {champ.printable()} has incorrect cdragon str '{champ._str_cdragon}'"
            )


if __name__ == "__main__":
    unittest.main()
