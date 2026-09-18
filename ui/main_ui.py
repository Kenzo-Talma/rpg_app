from PySide6.QtWidgets import QWidget, QVBoxLayout, QMainWindow

from ui.character_sheet import CharacterSheet


class mainUi(QMainWindow):
    def __init__(self):
        super().__init__()

        # main_layout :QVBoxLayout = QVBoxLayout(self)
        self.setStyleSheet("background-color: #3d3d3d;" \
                           "color: #b5b5b5")
        # self.setLayout(main_layout)

        character_sheet = CharacterSheet()
        # main_layout.addWidget(character_sheet)
        self.setCentralWidget(character_sheet)
