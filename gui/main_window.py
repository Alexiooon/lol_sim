"""Main script for running DPS calc with a GUI."""
# pylint: disable=E0611,W0611
import logging
import os
import sys

from PySide6.QtCore import QSize, Qt, Signal, Slot

# from Pyside6.QtCore.Qt import QHorizontal
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSlider,
    QStatusBar,
    QWidget,
)

import champions

ICON_FOLDER = os.path.join(os.path.dirname(__file__), "icon")


class MainWindow(QMainWindow):
    """Main window for scouting tool."""

    def __init__(self, app: QApplication):
        """Init."""
        super().__init__()
        self.app = app
        self.setWindowTitle('DPS Calculation Tool')

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

    def __init__(self) -> None:
        """Init."""
        super().__init__()
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Create the champion list
        scrollable = QScrollArea()
        champion_widget = ChampionButtonMenuWidget(self)
        scrollable.setWidget(champion_widget)
        scrollable.setFixedWidth((60 + 7) * 10 + 20)

        # Create the champion display
        self.champion_info = ChampionInfoWidget()

        main_layout.addWidget(scrollable)
        main_layout.addWidget(self.champion_info)

    @Slot(str, name="LoadChampion")
    def champion_button_press(self, champ: str):
        """Load stats for a champion."""
        logging.debug("Recieve signal '%s'", champ)
        self.champion_info.set_champ(champ)


class ChampionButtonMenuWidget(QWidget):
    """Widget containing buttons for all champions with icons."""

    def __init__(self, parent: MainDisplay) -> None:
        """Init."""
        super().__init__()
        self.setLayout(ChampionButtonLayout(parent))
        self.setFixedWidth((60 + 7) * 10)  # 10 champs per row, and a little margin in between


class ChampionButtonLayout(QGridLayout):
    """Grid with all champions as buttons."""

    def __init__(self, parent: MainDisplay) -> None:
        """Init."""
        super().__init__()
        n_cols = 10
        for i, champ in enumerate(os.listdir(ICON_FOLDER)):
            col = i % n_cols
            row = (i - col) / 10
            button = ChampionButton(champ[:-4])
            button.click_signal.connect(parent.champion_button_press)
            self.addWidget(button, row, col)


class ChampionButton(QPushButton):
    """QPushButton with a champion for icon."""

    icon_width = 60
    icon_height = 60
    click_signal = Signal(str, name="LoadChampion")

    def __init__(self, champ: str):
        """Init."""
        super().__init__()
        self.champ = champ
        self.clicked.connect(self.handle_button)

        # Set the image
        icon_path = os.path.join(ICON_FOLDER, champ + ".png")
        if os.path.exists(icon_path):
            self.setIcon(QIcon(icon_path))
            self.setIconSize(QSize(self.icon_width, self.icon_height))
            self.setFixedSize(self.icon_width, self.icon_height)
        else:
            logging.warning("Image not available for '%s'", champ)

    def handle_button(self):
        """Print the name of the champion."""
        logging.debug("Emit signal '%s'", self.champ)
        self.click_signal.emit(self.champ)


class ChampionInfoWidget(QFrame):
    """Sidebar containing info regarding a champion."""

    def __init__(self) -> None:
        """Init."""
        super().__init__()
        self.setFixedSize(250, 400)
        self.setFrameStyle(QFrame.StyledPanel)
        self.setLineWidth(1)
        self._layout = QGridLayout()
        self.setLayout(self._layout)

        # Champion definition
        self.champ: None | champions.BaseChampion = None
        self.champ_icon = QLabel()
        self.champ_title = QLabel()

        # Level slider
        self.level_slider = QSlider(Qt.Horizontal)
        self.level_slider.setMinimum(1)
        self.level_slider.setMaximum(18)
        self.level_slider.valueChanged.connect(self.update)        

        # Champion stats
        self.champ_stats = {
            "attack_damage": QLabel(),
            "attack_speed": QLabel(),
            "max_hp": QLabel(),
            "armor": QLabel(),
            "magic_resist": QLabel()
        }
        stat_row = 2  # Start row for champion stats
        for stat, val in self.champ_stats.items():
            stat_name_label = QLabel()
            stat_name_label.setText(stat)
            self._layout.addWidget(stat_name_label, stat_row, 0)
            self._layout.addWidget(val, stat_row, 1)
            stat_row += 1

        self._layout.addWidget(self.champ_icon, 0, 0)
        self._layout.addWidget(self.champ_title, 0, 1)
        self._layout.addWidget(self.level_slider, 1, 0, 1, 2)

    def set_champ(self, champ: str):
        """Set the champion to display."""
        icon_path = os.path.join(ICON_FOLDER, champ + ".png")
        if os.path.exists(icon_path):
            pixmap = QPixmap(icon_path)
            pixmap = pixmap.scaled(60, 60)
            self.champ_icon.setPixmap(pixmap)
        self.champ = getattr(champions, champ)()
        self.champ_title.setText(champ)
        self._layout.update()

    def update(self):
        """Update champion info."""
        self.champ.level = self.level_slider.value()
        for stat, val in self.champ_stats.items():
            val.setText(str(getattr(self.champ, stat)))


def main():
    """Run main functionality."""
    app = QApplication(sys.argv)
    window = MainWindow(app)
    window.setWindowTitle('LoL DPS Calc')

    # Unused Slider example
    # slider = QSlider(Qt.Horizontal)
    # slider.setMinimum(1)
    # slider.setMaximum(100)
    # slider.setValue(25)
    # slider.show()

    # Window
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
