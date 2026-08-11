from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from ui.character_sheet import CharacterSheet


class mainUi(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout(self)
        character_sheet = CharacterSheet()
        main_layout.addWidget(character_sheet)