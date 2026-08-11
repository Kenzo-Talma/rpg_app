import sys
from PySide6.QtWidgets import QApplication

import ui.main_ui as main_ui


if __name__ == "__main__":
    app = QApplication([])

    main_ui = main_ui.mainUi()
    main_ui.show()

    sys.exit(app.exec())
