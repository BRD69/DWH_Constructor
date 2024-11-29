from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QPushButton


class UiButtonsTest(QPushButton):
    def __init__(self, parent, name='', event_click=None):
        super(UiButtonsTest, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.event_click = event_click

        self._setup_ui()
        self._load_style_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName(f'btn_{self.name}_test')
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setText('Тест')

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


class UiButtonsSave(QPushButton):
    def __init__(self, parent, name='', event_click=None):
        super(UiButtonsSave, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.event_click = event_click

        self._icon = QtGui.QIcon()
        self._icon.addPixmap(QtGui.QPixmap(f":/form_sql/static/imgs/sub_form_sql/save.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self._setup_ui()
        self._load_style_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName(f'btn_{self.name}')
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setIcon(self._icon)
        self.setText("Сохранить")

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


class UiButtonsRun(QPushButton):
    def __init__(self, parent, name='', event_click=None):
        super(UiButtonsRun, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.event_click = event_click

        self._icon = QtGui.QIcon()
        self._icon.addPixmap(QtGui.QPixmap(f":/form_sql/static/imgs/sub_form_sql/run.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self._setup_ui()
        self._load_style_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName(f'btn_{self.name}')
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setIcon(self._icon)
        self.setText('Выполнить')

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


class UiButtonsCopy(QPushButton):
    def __init__(self, parent, name='', event_click=None):
        super(UiButtonsCopy, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.event_click = event_click

        self._icon = QtGui.QIcon()
        self._icon.addPixmap(QtGui.QPixmap(f":/form_command_infa/static/imgs/sub_form_command_infa/copy.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self._setup_ui()
        self._load_style_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName(f'btn_{self.name}')
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setIcon(self._icon)
        self.setText("Скопировать")

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
