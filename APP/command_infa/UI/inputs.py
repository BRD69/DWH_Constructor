from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QLineEdit, QSizePolicy


class UiLineEdit(QLineEdit):
    def __init__(self, parent=None, name=None, read_only=False, is_password=False, key_option=''):
        super(UiLineEdit, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.key_option = key_option
        self.read_only = read_only
        self.is_password = is_password
        self._height = 24

        self._setup_ui()
        self._load_style_ui()

    def _setup_ui(self):
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setObjectName(f"edit_{self.name}")
        self.setMinimumSize(QSize(0, self._height))
        self.setMaximumSize(QSize(16777215, self._height))
        self.setSizePolicy(size_policy)
        self.setReadOnly(self.read_only)
        if self.is_password:
            self.setEchoMode(QLineEdit.Password)

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           "    padding-left:3px;\n"
                           "    border: 1px solid rgb(180, 180, 180);\n"
                           "    border-radius: 3px;\n"
                           "}\n")

