import sys
from PySide6.QtWidgets import QApplication


import ui.main_ui


if __name__ == "__main__":
    app = QApplication([])
    app.setApplicationDisplayName("DnD utils")
    app.setStyleSheet("background-color: #3d3d3d;" \
                           "color: #b5b5b5")

    main_ui = ui.main_ui.mainUi()
    main_ui.show()

    sys.exit(app.exec())
