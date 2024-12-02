from PyQt5 import QtWidgets, QtCore

from APP.formated_xsd.sub_main import UiFormatedXSDForm
from APP.command_infa.sub_main import UiSubMainWindowCommandInfa
from APP.generator_sql.sub_main import UiSQLSubForm
from UI.widgets.actions import *


class UiMainWindow(QtWidgets.QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.ui_title = app.ui_title
        self.ui_width = app.ui_width
        self.ui_height = app.ui_height
        self.ui_icon = app.ui_icon

        self.sub_form_sql = None
        self.sub_form_command_infa = None
        self.sub_form_formated_xsd = None

        self._setup_ui()
        self._connect_sub_form()

    def _setup_ui(self):
        self.setObjectName("MainWindow")
        self.resize(self.ui_width, self.ui_height)
        self.setWindowTitle(self.ui_title)
        self.setWindowIcon(self.ui_icon)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")

        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 24))
        self.menubar.setObjectName("menubar")

        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_file.setTitle("Файл")

        self.menu_apps = QtWidgets.QMenu(self.menubar)
        self.menu_apps.setObjectName("menu_apps")
        self.menu_apps.setTitle("Приложения")

        self.setMenuBar(self.menubar)

        self.menu_file.addAction(ActionClose(self, self))
        self.menu_apps.addAction(ActionSQL(self, self))
        self.menu_apps.addAction(ActionCommandINFA(self, self))
        self.menu_apps.addAction(ActionDataProcessorXSD(self, self))
        self.menu_apps.addSeparator()
        self.menu_apps.addAction(ActionHamsterINI(self, self))
        # self.menu_apps.addSeparator()
        # self.menu_apps.addAction(ActionWallpapers(self, self))
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_apps.menuAction())

        QtCore.QMetaObject.connectSlotsByName(self)

    def _connect_sub_form(self):
        print("_connect_sub_form")
        # self.sub_form_sql = UiSQLSubForm(self.mdiArea, self)
        # self.sub_form_command_infa = UiSubMainWindowCommandInfa(self.mdiArea, self)
        # self.sub_form_formated_xsd = UiFormatedXSDForm(self.mdiArea, self)
        # self.mdiArea.addSubWindow(self.sub_form_sql)

    def action_close(self):
        self.close()

    def action_open_sql(self):
        self.sub_form_sql = UiSQLSubForm(self.mdiArea, self)
        self.mdiArea.addSubWindow(self.sub_form_sql)
        self.sub_form_sql.show()

    def action_open_command_infa(self):
        self.sub_form_command_infa = UiSubMainWindowCommandInfa(self.mdiArea, self)
        self.mdiArea.addSubWindow(self.sub_form_command_infa)
        self.sub_form_command_infa.show()

    def action_open_data_processor_xsd(self):
        self.sub_form_formated_xsd = UiFormatedXSDForm(self.mdiArea, self)
        self.mdiArea.addSubWindow(self.sub_form_formated_xsd)
        self.sub_form_formated_xsd.show()

    def action_open_hamster_ini(self):
        print("action_open_hamster_ini")

    def action_open_wallpapers(self):
        print("open_wallpapers")
