import json
from PySide6.QtWidgets import QDialog, QMenu, QMainWindow, QVBoxLayout, QFrame, QHBoxLayout, QLabel, QLineEdit, QMenuBar, QPushButton

from ui.character_sheet import CharacterSheet


class mainUi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.database_location :str = str()
        self.database_path :str = str()
        self.info_path :str = "{}\\data.json".format(__file__.rpartition("\\")[0])
        self.read_file_path()

        self.setStyleSheet("background-color: #3d3d3d;" \
                           "color: #b5b5b5")

        self.menu_bar :QMenuBar = self.menuBar()

        self.file_menu :QMenu = QMenu("file")
        self.menu_bar.addMenu(self.file_menu)

        self.file_menu.addAction(
            "change file location", self.open_file_location_dialog)

        character_sheet = CharacterSheet(self.database_path)
        self.setCentralWidget(character_sheet)


    def read_file_path(self):
        try:
            file_path = open(self.info_path, "r")
            data_dict :dict = json.load(file_path)
            self.database_location = data_dict["database_location"]
            self.database_path = f"{self.database_location}\\ttrpg_database.db"
        except Exception as e:
            file_path = open(self.info_path, "w+")
            self.database_location = self.info_path.rpartition("\\")[0]
            self.database_path = f"{self.database_location}\\ttrpg_database.db"
            self.write_file_path()


    def write_file_path(self):
        file_path = open(self.info_path, "w+")
        data_dict :dict = {
            "database_location": self.database_location
        }
        json.dump(data_dict, file_path)
        print(self.database_location)


    def open_file_location_dialog(self):
        file_location_dialog :FileLocationUi = FileLocationUi(self)
        file_location_dialog.exec_()
        if not file_location_dialog.result == 0:
            self.write_file_path()

        print(self.database_location)


class FileLocationUi(QDialog):
    def __init__(self, parent :mainUi):
        self.parent_class = parent
        self.database_location :str = self.parent_class.database_location
        super().__init__(parent=parent)

        self.main_layout :QVBoxLayout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.file_widget :QFrame = QFrame()
        self.main_layout.addWidget(self.file_widget)
        self.file_layout :QHBoxLayout = QHBoxLayout()
        self.file_widget.setLayout(self.file_layout)

        self.file_label :QLabel = QLabel("database location")
        self.file_layout.addWidget(self.file_label)
        self.file_line :QLineEdit = QLineEdit(self.database_location)
        self.file_layout.addWidget(self.file_line)
        self.file_line.textChanged.connect(self.database_location)

        self.accept_button :QPushButton = QPushButton("DONE")
        self.main_layout.addWidget(self.accept_button)
        self.accept_button.clicked.connect(self.accept)

    def database_location(self):
        self.parent_class.database_location = self.file_line.text()
