"""
ГЛАВНЫЙ МОДУЛЬ ЗАПУСКА ПРИЛОЖЕНИЯ
Описание:
    todo: придумать хорошее описание
Классы:
    - Application - Приложение
    - AppMainWindow - Главное окно приложения
"""

import os
import sys

import settings

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.forms.main import UiMainWindow


# Определение пути приложения в исполняемом файле Python, сгенерированном PyInstaller
if getattr(sys, 'frozen', False):
    Current_Path = os.path.dirname(sys.executable)
else:
    Current_Path = str(os.path.dirname(__file__))


class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setWindowIcon(QtGui.QIcon("icon512.ico"))


class AppMainWindow(QMainWindow):
    def __init__(self):
        _icon_logo = QtGui.QIcon()
        _icon_logo.addPixmap(QtGui.QPixmap(":/main_form/static/imgs/main_form/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        super(AppMainWindow, self).__init__()

        # НАСТРОЙКИ ПРИЛОЖЕНИЯ
        self.settings = settings.Settings()
        self.ui_icon = _icon_logo  # иконка приложения
        self.ui_title = self.settings.title  # заголовок приложения
        self.ui_width = self.settings.screen_width  # размеры приложения (ширина)
        self.ui_height = self.settings.screen_height  # размеры приложения (высота)

        self.ui = UiMainWindow(self)



import resource

if __name__ == '__main__':
    app = Application(sys.argv)

    window = AppMainWindow()
    window.ui.show()

    sys.exit(app.exec_())
