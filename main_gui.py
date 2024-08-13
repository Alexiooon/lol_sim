#!/usr/bin/env python3
# pylint: disable=E0611,W0611
"""Base file for some testing with GUI."""
import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow


def main():
    """Execute demo functionality."""
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.setWindowTitle('LoL DPS Calc')
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
