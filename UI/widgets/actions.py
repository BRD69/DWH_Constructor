from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction


class ActionClose(QAction):
    def __init__(self, parent, main_form):
        super(ActionClose, self).__init__(parent)
        self.main_form = main_form
        self.setObjectName("action_exit")
        self.setIcon(QIcon(":/main_form/static/imgs/main_form/close.png"))
        self.setText("Выход")
        self.triggered.connect(self.main_form.action_close)


class ActionSQL(QAction):
    def __init__(self, parent, main_form):
        super(ActionSQL, self).__init__(parent)
        self.main_form = main_form
        self.setObjectName("action_sql")
        self.setIcon(QIcon(":/main_form/static/imgs/main_form/sql.png"))
        self.setText("Генератор SQL")
        self.triggered.connect(self.main_form.action_open_sql)


class ActionCommandINFA(QAction):
    def __init__(self, parent, main_form):
        super(ActionCommandINFA, self).__init__(parent)
        self.main_form = main_form
        self.setObjectName("action_command_infa")
        self.setIcon(QIcon(":/main_form/static/imgs/main_form/command_infa.png"))
        self.setText("Команды INFA")
        self.triggered.connect(self.main_form.action_open_command_infa)


class ActionDataProcessorXSD(QAction):
    def __init__(self, parent, main_form):
        super(ActionDataProcessorXSD, self).__init__(parent)
        self.main_form = main_form
        self.setObjectName("action_data_processor_xsd")
        self.setIcon(QIcon(":/main_form/static/imgs/main_form/data_processor_xsd.png"))
        self.setText("Форматирование XSD")
        self.triggered.connect(self.main_form.action_open_data_processor_xsd)


class ActionBoberINI(QAction):
    def __init__(self, parent, main_form):
        super(ActionBoberINI, self).__init__(parent)
        self.main_form = main_form
        self.setObjectName("action_bober_ini")
        # self.setIcon()
        self.setText("Bober")
        self.triggered.connect(self.main_form.action_open_bober_ini)


class ActionWallpapers(QAction):
    def __init__(self, parent, main_form):
        super(ActionWallpapers, self).__init__(parent)
        self.main_form = main_form
        self.setObjectName("action_wallpapers")
        # self.setIcon()
        self.setText("Wallpapers")
        self.triggered.connect(self.main_form.action_open_wallpapers)
