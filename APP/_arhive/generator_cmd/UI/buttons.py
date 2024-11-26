"""
МОДУЛЬ ЭЛЕМЕНТОВ УПРАВЛЕНИЯ ОСНОВНЫМИ ФУНКЦИЯМИ ПРИЛОЖЕНИЯ
Описание:
    todo: придумать хорошее описание

Классы:
    - AboutButton - кнопка об авторе
    - ...
"""
import pyperclip
from PyQt5.QtCore import QSize, Qt, QTimer
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import (
    QPushButton, QSizePolicy
)

from APP._arhive.generator_cmd.UI.forms import UiDialogText


class ViewButton(QPushButton):
    def __init__(self, parent, window_main=None, app=None, name="", element=None):
        h, w = 24, 24
        _icon = QIcon()
        _icon.addPixmap(QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/view.png"), QIcon.Normal, QIcon.Off)

        super().__init__(parent)
        self.parent = parent
        self.window_main = window_main
        self.app_main = app

        self.size = QSize(w, h)
        self.icon = _icon

        self.name = name
        self.element = element

        """ФУНКЦИИ ЗАГРУЗКИ ИНТЕРФЕЙСА И ДАННЫХ"""
        self._setup_ui()
        self._load_style_ui()
        self._connect_events()

    def _setup_ui(self):
        self.setObjectName(f"view_button_{self.name}")

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        # self.setFixedSize(self.size)
        self.setMinimumSize(self.size)
        self.setMaximumSize(self.size)
        self.setCursor(Qt.PointingHandCursor)
        self.setIcon(self.icon)

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           f"    border: 1px solid rgb(167, 167, 167);\n"
                           f"    background: rgb(242, 242, 242);\n"
                           f"    padding: 0px;\n"
                           # f"    background: rgb(30, 242, 10);\n"
                           # f"    font-size: 14px;\n"
                           f"    border-radius: 3px;\n"
                           "}\n"
                           f"#{self.objectName()}:hover"
                           "{\n"
                           f"    background-color: rgba(200, 200, 200, 128);\n"
                           "}\n"
                           f"#{self.objectName()}:pressed"
                           "{\n"
                           f"    background-color: rgba(255, 255, 255, 128);\n"
                           "}\n")

    def _connect_events(self):
        self.clicked.connect(lambda: self._clicked_btn_view(text=self.element.text(), title=""))

    def _clicked_btn_view(self, text, title):
        dialog = UiDialogText(text=text, title=title)
        dialog.setModal(True)
        dialog.exec_()


class CopyButton(QPushButton):
    def __init__(self, parent, window_main=None, app=None, name="", element=None):
        h, w = 24, 65
        _icon = QIcon()
        _icon.addPixmap(QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/copy.png"), QIcon.Normal, QIcon.Off)

        super().__init__(parent)

        self.parent = parent
        self.window_main = window_main
        self.app_main = app

        self.size = QSize(w, h)
        self.icon = _icon

        self.name = name
        self.element = element

        self.timer = QTimer(self)

        """ФУНКЦИИ ЗАГРУЗКИ ИНТЕРФЕЙСА И ДАННЫХ"""
        self._setup_ui()
        self._load_style_ui()
        self._connect_events()

    def _setup_ui(self):
        self.setObjectName(f"copy_button_{self.name}")
        self.setFixedSize(self.size)
        self.setCursor(Qt.PointingHandCursor)
        self.setIcon(self.icon)
        self.setText("Copy")

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           f"    border: 1px solid rgb(167, 167, 167);\n"
                           f"    background: rgb(242, 242, 242);\n"
                           f"    padding: 3px;\n"
                           f"    margin: 0px;\n"
                           f"    font-size: 11px;\n"
                           f"    border-radius: 3px;\n"
                           "}\n"
                           f"#{self.objectName()}:hover"
                           "{\n"
                           f"    background-color: rgba(200, 200, 200, 128);\n"
                           "}\n"
                           f"#{self.objectName()}:pressed"
                           "{\n"
                           f"    background-color: rgba(255, 255, 255, 128);\n"
                           "}\n")
        self._style_element_copy = (f"#{self.element.objectName()}"
                                    "{\n"
                                    f"    background-color: rgba(12, 242, 34, 30);\n"
                                    f"    padding-left:3px;\n"
                                    f"    border: 1px solid rgb(180, 180, 180);\n"
                                    f"    border-radius: 3px;\n"
                                    "}\n")
        self._style_element_orig = (f"#{self.element.objectName()}"
                                    "{\n"
                                    f"    background-color: none;\n"
                                    f"    padding-left:3px;\n"
                                    f"    border: 1px solid rgb(180, 180, 180);\n"
                                    f"    border-radius: 3px;\n"
                                    "}\n")

    def _connect_events(self):
        self.clicked.connect(lambda: self._copy_text(self.element.text()))
        self.timer.timeout.connect(self._signal_timer)

    def _copy_text(self, text):
        pyperclip.copy(text)
        self.element.setStyleSheet(self._style_element_copy)
        self.timer.start(150)

    def _signal_timer(self):
        self.element.setStyleSheet(self._style_element_orig)
        self.timer.stop()
