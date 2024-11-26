from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QPushButton


class UiButtonsViewCopy(QPushButton):
    def __init__(self, parent, name='', event_click=None, type_btn='', border_radius=(0, 0, 0, 0)):
        super(UiButtonsViewCopy, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.event_click = event_click
        self.type_btn = type_btn
        self.border_radius = border_radius

        self._icon_name = f"{type_btn}.png"

        self._icon = QtGui.QIcon()
        self._icon.addPixmap(QtGui.QPixmap(f":/form_command_infa/static/imgs/sub_form_command_infa/{self._icon_name}"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self._setup_ui()
        self._load_style_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName(f'btn_{self.name}_{self.type_btn}')
        self.setMaximumSize(QtCore.QSize(35, 16777215))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setIcon(self._icon)
        self.setText("")

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           "    border: 1px solid rgb(167, 167, 167);\n"
                           "    background: rgb(242, 242, 242);\n"
                           "    padding: 3px;\n"
                           "    font-size: 11px;\n"
                           f"    border-top-left-radius: {self.border_radius[0]}px;\n"
                           f"    border-top-right-radius: {self.border_radius[1]}px;\n"
                           f"    border-bottom-left-radius: {self.border_radius[2]}px;\n"
                           f"    border-bottom-right-radius: {self.border_radius[3]}px;\n"
                           "}\n"
                           f"#{self.objectName()}:hover"
                           "{\n"
                           "    background-color: rgba(200, 200, 200, 128);\n"
                           "}\n"
                           f"#{self.objectName()}:pressed"
                           "{\n"
                           "    background-color: rgba(255, 255, 255, 128);\n"
                           "}")

    def _connect_event(self):
        if self.event_click:
            self.clicked.connect(self.event_click)


class UiButtonsHelp(QPushButton):
    def __init__(self, parent, name='', event_click=None):
        super(UiButtonsHelp, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.event_click = event_click

        self._setup_ui()
        self._load_style_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName(f'btn_{self.name}_help')
        self.setMinimumSize(QtCore.QSize(25, 16))
        self.setMaximumSize(QtCore.QSize(20, 16777215))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setText('?')

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           "    border: none;\n"
                           "    padding: 3px;\n"
                           "    font-size: 13px;\n"
                           "    border-radius: 3px;\n"
                           "}\n"
                           f"#{self.objectName()}:hover"
                           "{\n"
                           "    background-color: rgba(200, 200, 200, 128);\n"
                           "}\n"
                           f"#{self.objectName()}:pressed"
                           "{\n"
                           "    background-color: rgba(255, 255, 255, 128);\n"
                           "}")

    def _connect_event(self):
        if self.event_click:
            self.clicked.connect(self.event_click)


class UiButtonsRun(QPushButton):
    def __init__(self, parent, name='', event_click=None):
        super(UiButtonsRun, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.event_click = event_click

        self._icon = QtGui.QIcon()
        self._icon.addPixmap(QtGui.QPixmap(f":/form_command_infa/static/imgs/sub_form_command_infa/start.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self._setup_ui()
        self._load_style_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName(f'btn_{self.name}_run')
        self.setMinimumSize(QtCore.QSize(70, 0))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setIcon(self._icon)
        self.setText('Run')

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           "    border: 1px solid rgb(167, 167, 167);\n"
                           "    background: rgb(242, 242, 242);\n"
                           "    padding: 3px;\n"
                           "    font-size: 11px;\n"
                           "    border-top-left-radius: 3px;\n"
                           "    border-top-right-radius: 0;\n"
                           "    border-bottom-left-radius: 3px;\n"
                           "    border-bottom-right-radius: 0;\n"
                           "}\n"
                           f"#{self.objectName()}:hover"
                           "{\n"
                           "    background-color: rgba(200, 200, 200, 128);\n"
                           "}\n"
                           f"#{self.objectName()}:pressed"
                           "{\n"
                           "    background-color: rgba(255, 255, 255, 128);\n"
                           "}")

    def _connect_event(self):
        if self.event_click:
            self.clicked.connect(self.event_click)


class UiButtonsOpenDialog(QPushButton):
    def __init__(self, parent, name='', event_click=None):
        super(UiButtonsOpenDialog, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.event_click = event_click

        self._setup_ui()
        self._load_style_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName(f'btn_settings_{self.name}_open_dialog')
        self.setMinimumSize(QtCore.QSize(28, 22))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setText('...')

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           "    border: 1px solid rgb(167, 167, 167);\n"
                           "    background: rgb(242, 242, 242);\n"
                           "    padding: 3px;\n"
                           "    font-size: 11px;\n"
                           "    border-radius: 3px;\n"
                           "}\n"
                           f"#{self.objectName()}:hover"
                           "{\n"
                           "    background-color: rgba(200, 200, 200, 128);\n"
                           "}\n"
                           f"#{self.objectName()}:pressed"
                           "{\n"
                           "    background-color: rgba(255, 255, 255, 128);\n"
                           "}")

    def _connect_event(self):
        if self.event_click:
            self.clicked.connect(self.event_click)
