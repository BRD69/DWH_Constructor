from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QLineEdit, QWidget, QLabel


class UiLineEdit(QLineEdit):
    def __init__(self, parent=None, name=None):
        super(UiLineEdit, self).__init__(parent)
        self.parent = parent
        self.name = name
        self._height = 24

        self._setup_ui()
        self._load_style_ui()

    def _setup_ui(self):
        self.setObjectName(f"edit_{self.name}")
        self.setMinimumSize(QSize(0, self._height))
        self.setMaximumSize(QSize(16777215, self._height))

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           "    padding-left:3px;\n"
                           "    border: 1px solid rgb(180, 180, 180);\n"
                           "    border-radius: 3px;\n"
                           "}\n")


class UiLabelIcon(QLabel):
    def __init__(self, parent=None, name=None):
        super(UiLabelIcon, self).__init__(parent)
        self.parent = parent
        self.name = name
        self._h = 16
        self._w = 16

    def _setup_ui(self):
        self.setObjectName(f"label_{self.name}")
        self.setMinimumSize(QSize(self._w, self._h))
        self.setMaximumSize(QSize(self._w, self._h))
        self.setBaseSize(QSize(self._w, self._h))
        self.setText("")
