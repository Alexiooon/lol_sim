"""Main script for running DPS calc with a GUI."""
# pylint: disable=E0611,W0611
import logging
import os
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QStatusBar,
    QWidget,
)


class MainWindow(QMainWindow):
    """Main window for scouting tool."""

    def __init__(self, app: QApplication):
        """Init."""
        super().__init__()
        self.app = app
        self.setWindowTitle('Scouting Tool')

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')
        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)

        self.setStatusBar(QStatusBar(self))
        self.statusBar().showMessage('Initialized')

        self.setCentralWidget(MainDisplay())

    def quit_app(self):
        """Close the application."""
        self.app.quit()


class MainDisplay(QWidget):
    """Example widget."""

    def __init__(self):
        """Init."""
        super().__init__()
        button1 = QPushButton('Button1')
        button2 = ChampionButton('Aatrox')

        button1.clicked.connect(self.click_button)
        button2.clicked.connect(self.click_button)

        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        # self.setLayout(button_layout)

        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # self.setLayout(ChampionButtonMenu())
        scrollable = QScrollArea()
        champion_widget = ChampionButtonMenuWidget()
        champion_widget.setLayout(ChampionButtonLayout())
        scrollable.setWidget(champion_widget)
        scrollable.setFixedWidth((60 + 7) * 10 + 20)
        main_layout.addChildWidget(scrollable)

    def click_button(self):
        """Click the button."""
        print(f'Hehe, {self}')


class ChampionButtonMenuWidget(QWidget):
    """Widget containing buttons for all champions with icons."""

    def __init__(self):
        """Init."""
        super().__init__()
        self.setFixedWidth((60 + 7) * 10)  # 10 champs per row, and a little margin in between


class ChampionButtonLayout(QGridLayout):
    """Grid with all champions as buttons."""

    def __init__(self):
        """Init."""
        super().__init__()
        n_cols = 10
        for i, champ in enumerate(os.listdir("icon")):
            col = i % n_cols
            row = (i - col) / 10
            self.addWidget(ChampionButton(champ[:-4]), row, col)


class ChampionButton(QPushButton):
    """QPushButton with a champion for icon."""

    icon_width = 60
    icon_height = 60

    def __init__(self, champ: str):
        """Init."""
        super().__init__()
        self.champ = champ
        self.clicked.connect(self.handle_button)

        # Set the image
        icon_path = os.path.join("icon", champ + ".png")
        if os.path.exists(icon_path):
            self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(self.icon_width, self.icon_height))
            self.setFixedSize(self.icon_width, self.icon_height)
        else:
            logging.warning("Image not available for '%s'", champ)

    def handle_button(self):
        """Print the name of the champion."""
        print(self.champ)


def main():
    """Run main functionality."""
    app = QApplication(sys.argv)

    # window = QMainWindow()
    window = MainWindow(app)
    window.setWindowTitle('LoL DPS Calc')
    # window = QWidget()

    # Slider
    # slider = QSlider(Qt.Horizontal)
    # slider.setMinimum(1)
    # slider.setMaximum(100)
    # slider.setValue(25)
    # slider.show()

    # Window
    # window.setCentralWidget(button)
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
