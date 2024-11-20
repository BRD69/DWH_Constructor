"""
МОДУЛЬ ПАНЕЛЕЙ УПРАВЛЕНИЯ ПРИЛОЖЕНИЯ
Описание:
    todo: придумать хорошее описание

Классы:
    - UiMainTitleBar - панель заголовок
    - UiGroupBox - группа в которой команда и кнопки
    - ...
"""
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QSizePolicy


class UiGroupBox(QGroupBox):
    def __init__(self, parent=None, name="", name_icon="", app=None):
        h = 75
        super().__init__(parent)
        self.app = app
        self._height = h
        self.name = f"groupbox_{name}"

        self.mode_link = ""
        if name_icon.upper() in ["WF", "APP"]:
            self.mode_link = name_icon.upper()

        self.name_icon = "APP.png"
        if name_icon:
            self.name_icon = f"{name_icon.upper()}.png"

        """ФУНКЦИИ ЗАГРУЗКИ ИНТЕРФЕЙСА И ДАННЫХ"""
        self._setup_ui()
        self._load_style_ui()

    def _setup_ui(self):
        self.setObjectName(self.name)
        self.setMaximumHeight(self._height)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.setCheckable(True)
        self.setChecked(True)
        if self.mode_link:
            self.setCursor(Qt.PointingHandCursor)

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}:title"
                           "{\n"
                           f"    subcontrol-origin: margin;\n"
                           f"    padding-left: 10px;\n"
                           "}\n"
                           f"#{self.objectName()}::indicator:unchecked"
                           "{\n"
                           f"    image: url(:/form_command_infa/static/imgs/sub_form_command_infa/{self.name_icon});\n"
                           "}\n"
                           f"#{self.objectName()}::indicator:checked"
                           "{\n"
                           f"    image: url(:/form_command_infa/static/imgs/sub_form_command_infa/{self.name_icon});\n"
                           "}\n")

    def mousePressEvent(self, event):
        if self.mode_link == "WF":
            webbrowser.open(
                'https://docs.informatica.com/data-engineering/common-content-for-data-engineering/10-4-1/command-reference/infacmd-wfs-command-reference/startworkflow.html')
        if self.mode_link == "APP":
            webbrowser.open(
                'https://docs.informatica.com/data-engineering/common-content-for-data-engineering/10-4-1/command-reference/infacmd-dis-command-reference/startapplication.html')


class UiHBoxLayout(QHBoxLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setObjectName(f"horizontalLayout_{parent.objectName()}")
        # self.setContentsMargins(5, 5, 5, 5)
        # self.setSpacing(5)
