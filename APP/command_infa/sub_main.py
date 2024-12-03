import os.path
import webbrowser

import pyperclip
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget, QDialogButtonBox, QFileDialog, QRadioButton

from APP.command_infa.UI.buttons import UiButtonsViewCopy, UiButtonsHelp, UiButtonsRun, UiButtonsOpenDialog, \
    UiButtonsInfa
from APP.command_infa.UI.forms import UiDialogText
from APP.command_infa.UI.inputs import UiLineEdit
from APP.command_infa.UI.panels import UiLineFrame, UiFrame
from APP.command_infa.core import TemplatesCMD, SettingsCMD, ModeButton


def get_index(array, param):
    for index, value in enumerate(array):
        if param in value:
            return index


def get_position(text, param):
    if text:
        return text.index(param)
    else:
        return -1


class UiSubMainWindowCommandInfa(QWidget):
    def __init__(self, parent=None, main_window=None):
        w, h = 800, 700
        title = "Команды INFA"
        super(UiSubMainWindowCommandInfa, self).__init__(parent)

        self.app = main_window.app
        self.main_window = main_window
        self.timer = QTimer(self)

        self.mode = ModeButton
        self.settings_cmd = SettingsCMD(path=self.app.settings.dir_udata)
        self.templates_cmd = TemplatesCMD(path=self.app.settings.dir_settings)

        self.is_check_settings = False

        self._title = title
        self._w = w
        self._h = h
        self._sql_path_placeholder_text = os.path.join("C:", "SQLAgentJob", "IPC", "bat", "infacmd_proxy.bat")
        self._infa_path_placeholder_text = os.path.join("C:", "Informatica", "10.4.1", "clients", "DeveloperClient", "infacmd", "infacmd.bat")

        """ФУНКЦИИ ЗАГРУЗКИ ИНТЕРФЕЙСА И ДАННЫХ"""
        self._setup_ui()
        self._load_style_ui()
        self._load_data_ui()
        self._connect_events()

    def _setup_ui(self):
        self.setObjectName("SubMainWindowCommandInfa")
        self.setMinimumSize(QtCore.QSize(self._w, self._h))
        self.setWindowTitle(self._title)

        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 15)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.toolBox = QtWidgets.QToolBox(self)
        self.toolBox.setObjectName("toolBox")
        self.page_command = QtWidgets.QWidget()
        self.page_command.setGeometry(QtCore.QRect(0, 0, 800, 517))
        self.page_command.setObjectName("page_command")

        self.gridLayout = QtWidgets.QGridLayout(self.page_command)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")

        self.frame_btn_admin_monitor = UiFrame(self.page_command, name='btn_admin_monitor', border=True)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_btn_admin_monitor)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")

        self.frame_btn_monitor_left = UiFrame(self.frame_btn_admin_monitor, name='btn_monitor_left', border=False)

        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_btn_monitor_left)
        self.horizontalLayout_15.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_15.setSpacing(12)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")

        self.btn_infa_test = UiButtonsInfa(self.frame_btn_monitor_left, name='test')
        self.horizontalLayout_15.addWidget(self.btn_infa_test)

        self.line_0 = UiLineFrame(self.frame_btn_monitor_left, name='line_0', shape='V')
        self.horizontalLayout_15.addWidget(self.line_0)

        self.btn_infa_prod = UiButtonsInfa(self.frame_btn_monitor_left, name='prod')

        self.horizontalLayout_15.addWidget(self.btn_infa_prod)
        self.horizontalLayout_14.addWidget(self.frame_btn_monitor_left)

        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacer_item)

        self.gridLayout.addWidget(self.frame_btn_admin_monitor, 0, 0, 1, 1)

        self.groupbox_input = UiFrame(self.page_command, name='input', border=True)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupbox_input)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Область DMN -------------------------------------------------------
        self.frame1_DMN = QtWidgets.QFrame(self.groupbox_input)
        self.frame1_DMN.setObjectName("frame1_DMN")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame1_DMN)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_icon_DMN = QtWidgets.QLabel(self.frame1_DMN)
        self.lbl_icon_DMN.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_DMN.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_DMN.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_DMN.setText("")
        self.lbl_icon_DMN.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/DMN.png"))
        self.lbl_icon_DMN.setObjectName("lbl_icon_DMN")
        self.horizontalLayout.addWidget(self.lbl_icon_DMN)
        self.lbl_text_DMN = QtWidgets.QLabel(self.frame1_DMN)
        self.lbl_text_DMN.setMinimumSize(QtCore.QSize(35, 0))
        self.lbl_text_DMN.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lbl_text_DMN.setBaseSize(QtCore.QSize(35, 0))
        self.lbl_text_DMN.setStyleSheet("QLabel{\n"
                                        "    font-size: 13px;\n"
                                        "    font-weight: 500;\n"
                                        "}")
        self.lbl_text_DMN.setTextFormat(QtCore.Qt.AutoText)
        self.lbl_text_DMN.setScaledContents(False)
        self.lbl_text_DMN.setObjectName("lbl_text_DMN")
        self.horizontalLayout.addWidget(self.lbl_text_DMN)

        self.edit_DMN = UiLineEdit(self.frame1_DMN, "DMN", )
        self.edit_DMN.setText("")

        self.horizontalLayout.addWidget(self.edit_DMN)
        self.verticalLayout_3.addWidget(self.frame1_DMN)

        # Область DIS -------------------------------------------------------
        self.frame2_DIS = QtWidgets.QFrame(self.groupbox_input)
        self.frame2_DIS.setObjectName("frame2_DIS")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame2_DIS)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_icon_DIS = QtWidgets.QLabel(self.frame2_DIS)
        self.lbl_icon_DIS.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_DIS.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_DIS.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_DIS.setText("")
        self.lbl_icon_DIS.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/DIS.png"))
        self.lbl_icon_DIS.setObjectName("lbl_icon_DIS")
        self.horizontalLayout_2.addWidget(self.lbl_icon_DIS)
        self.lbl_text_DIS = QtWidgets.QLabel(self.frame2_DIS)
        self.lbl_text_DIS.setMinimumSize(QtCore.QSize(35, 0))
        self.lbl_text_DIS.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lbl_text_DIS.setBaseSize(QtCore.QSize(35, 0))
        self.lbl_text_DIS.setStyleSheet("QLabel{\n"
                                        "    font-size: 13px;\n"
                                        "    font-weight: 500;\n"
                                        "}")
        self.lbl_text_DIS.setObjectName("lbl_text_DIS")
        self.horizontalLayout_2.addWidget(self.lbl_text_DIS)

        self.edit_DIS = UiLineEdit(self.frame2_DIS, "DIS")
        self.edit_DIS.setText("")

        self.horizontalLayout_2.addWidget(self.edit_DIS)
        self.verticalLayout_3.addWidget(self.frame2_DIS)

        # Область APP -------------------------------------------------------
        self.frame3_APP = QtWidgets.QFrame(self.groupbox_input)
        self.frame3_APP.setObjectName("frame3_APP")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame3_APP)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_icon_APP = QtWidgets.QLabel(self.frame3_APP)
        self.lbl_icon_APP.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_APP.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_APP.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_APP.setText("")
        self.lbl_icon_APP.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/APP.png"))
        self.lbl_icon_APP.setObjectName("lbl_icon_APP")
        self.horizontalLayout_3.addWidget(self.lbl_icon_APP)
        self.lbl_text_APP = QtWidgets.QLabel(self.frame3_APP)
        self.lbl_text_APP.setMinimumSize(QtCore.QSize(35, 0))
        self.lbl_text_APP.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lbl_text_APP.setBaseSize(QtCore.QSize(35, 0))
        self.lbl_text_APP.setStyleSheet("QLabel{\n"
                                        "    font-size: 13px;\n"
                                        "    font-weight: 500;\n"
                                        "}")
        self.lbl_text_APP.setObjectName("lbl_text_APP")
        self.horizontalLayout_3.addWidget(self.lbl_text_APP)

        self.edit_APP = UiLineEdit(self.frame3_APP, "APP")
        self.edit_APP.setText("")

        self.horizontalLayout_3.addWidget(self.edit_APP)
        self.verticalLayout_3.addWidget(self.frame3_APP)

        # Область WF -------------------------------------------------------
        self.frame4_WF = QtWidgets.QFrame(self.groupbox_input)
        self.frame4_WF.setObjectName("frame4_WF")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame4_WF)
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_icon_WF = QtWidgets.QLabel(self.frame4_WF)
        self.lbl_icon_WF.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_WF.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_WF.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_WF.setText("")
        self.lbl_icon_WF.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/WF.png"))
        self.lbl_icon_WF.setObjectName("lbl_icon_WF")
        self.horizontalLayout_4.addWidget(self.lbl_icon_WF)
        self.lbl_text_WF = QtWidgets.QLabel(self.frame4_WF)
        self.lbl_text_WF.setMinimumSize(QtCore.QSize(35, 0))
        self.lbl_text_WF.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lbl_text_WF.setBaseSize(QtCore.QSize(35, 0))
        self.lbl_text_WF.setStyleSheet("QLabel{\n"
                                       "    font-size: 13px;\n"
                                       "    font-weight: 500;\n"
                                       "}")
        self.lbl_text_WF.setObjectName("lbl_text_WF")
        self.horizontalLayout_4.addWidget(self.lbl_text_WF)

        self.edit_WF = UiLineEdit(self.frame4_WF, "WF")
        self.edit_WF.setText("")

        self.horizontalLayout_4.addWidget(self.edit_WF)
        self.verticalLayout_3.addWidget(self.frame4_WF)

        # Область PS -------------------------------------------------------
        self.frame5_PS = QtWidgets.QFrame(self.groupbox_input)
        self.frame5_PS.setObjectName("frame5_PS")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame5_PS)
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lbl_icon_PS = QtWidgets.QLabel(self.frame5_PS)
        self.lbl_icon_PS.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_PS.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_PS.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_PS.setText("")
        self.lbl_icon_PS.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/PS.png"))
        self.lbl_icon_PS.setObjectName("lbl_icon_PS")
        self.horizontalLayout_5.addWidget(self.lbl_icon_PS)
        self.lbl_text_PS = QtWidgets.QLabel(self.frame5_PS)
        self.lbl_text_PS.setMinimumSize(QtCore.QSize(35, 0))
        self.lbl_text_PS.setMaximumSize(QtCore.QSize(35, 16777215))
        self.lbl_text_PS.setBaseSize(QtCore.QSize(35, 0))
        self.lbl_text_PS.setStyleSheet("QLabel{\n"
                                       "    font-size: 13px;\n"
                                       "    font-weight: 500;\n"
                                       "}")
        self.lbl_text_PS.setObjectName("lbl_text_PS")
        self.horizontalLayout_5.addWidget(self.lbl_text_PS)

        self.edit_PS = UiLineEdit(self.frame5_PS, "PS")
        self.edit_PS.setText("")

        self.horizontalLayout_5.addWidget(self.edit_PS)
        self.verticalLayout_3.addWidget(self.frame5_PS)
        self.gridLayout.addWidget(self.groupbox_input, 1, 0, 1, 1)
        self.groupbox_output = QtWidgets.QGroupBox(self.page_command)
        self.groupbox_output.setStyleSheet("#groupbox_output{\n"
                                           "    border: 1px solid rgb(137, 137, 137);\n"
                                           "    border-radius: 5px;\n"
                                           "    background-color: rgb(227, 227, 227);\n"
                                           "}")
        self.groupbox_output.setObjectName("groupbox_output")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox_output)
        self.verticalLayout.setObjectName("verticalLayout")

        # Область Agent SQL Job -------------------------------------------------------
        self.frame_1_sql_job = UiFrame(self.groupbox_output, name='1_sql_job', border=True)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_1_sql_job)

        self.horizontalLayout_8.setObjectName("horizontalLayout_8")

        self.frame_sql_job_title = UiFrame(self.frame_1_sql_job, name="sql_job_title", border=False)
        self.frame_sql_job_title.setMaximumWidth(270)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_sql_job_title)

        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_sql_job_icon = QtWidgets.QLabel(self.frame_sql_job_title)
        self.label_sql_job_icon.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_sql_job_icon.setText("")
        self.label_sql_job_icon.setPixmap(
            QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/SQL.png"))
        self.label_sql_job_icon.setObjectName("label_sql_job_icon")
        self.horizontalLayout_16.addWidget(self.label_sql_job_icon)
        self.label_sql_job_title = QtWidgets.QLabel(self.frame_sql_job_title)
        self.label_sql_job_title.setObjectName("label_sql_job_title")
        self.horizontalLayout_16.addWidget(self.label_sql_job_title)

        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacer_item)

        self.horizontalLayout_8.addWidget(self.frame_sql_job_title)

        self.line_4 = UiLineFrame(self.frame_1_sql_job, name='4', shape='v')
        self.horizontalLayout_8.addWidget(self.line_4)

        self.frame_sql_job_btn = QtWidgets.QFrame(self.frame_1_sql_job)
        self.frame_sql_job_btn.setObjectName("frame_sql_job_btn")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_sql_job_btn)

        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.cb_sql_job_wait = QtWidgets.QCheckBox(self.frame_sql_job_title)
        self.cb_sql_job_wait.setObjectName("cb_sql_job_wait")
        self.horizontalLayout_8.addWidget(self.cb_sql_job_wait)

        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacer_item)
        # Кнопки SQL Job ->
        self.btn_1_sql_job_view = UiButtonsViewCopy(self.frame_sql_job_btn,
                                                    name='1_sql_job',
                                                    event_click=None,
                                                    type_btn='view',
                                                    border_radius=(3, 0, 3, 0))
        self.horizontalLayout_6.addWidget(self.btn_1_sql_job_view)

        self.btn_2_sql_job_copy = UiButtonsViewCopy(self.frame_sql_job_btn,
                                                    name='2_sql_job',
                                                    event_click=None,
                                                    type_btn='copy',
                                                    border_radius=(0, 3, 0, 3))
        self.horizontalLayout_6.addWidget(self.btn_2_sql_job_copy)

        self.btn_3_sql_job_help = UiButtonsHelp(self.frame_sql_job_btn,
                                                name='3_sql_job',
                                                event_click=None)
        self.horizontalLayout_6.addWidget(self.btn_3_sql_job_help)
        # <- Кнопки SQL Job

        self.horizontalLayout_8.addWidget(self.frame_sql_job_btn)
        self.verticalLayout.addWidget(self.frame_1_sql_job)

        self.line = UiLineFrame(self.groupbox_output, name='0', shape='h')
        self.verticalLayout.addWidget(self.line)

        # Область Application -------------------------------------------------------
        self.frame_2_app = UiFrame(self.groupbox_output, name='2_app', border=True)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_2_app)

        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        self.frame_app_title = UiFrame(self.frame_2_app, name='app_title', border=False)
        self.frame_app_title.setMaximumWidth(270)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_app_title)

        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_app_icon = QtWidgets.QLabel(self.frame_app_title)
        self.label_app_icon.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_app_icon.setText("")
        self.label_app_icon.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/APP.png"))
        self.label_app_icon.setObjectName("label_app_icon")
        self.horizontalLayout_17.addWidget(self.label_app_icon)
        self.label_app_title = QtWidgets.QLabel(self.frame_app_title)
        self.label_app_title.setObjectName("label_app_title")
        self.horizontalLayout_17.addWidget(self.label_app_title)

        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacer_item)

        self.horizontalLayout_9.addWidget(self.frame_app_title)

        self.line_5 = UiLineFrame(self.frame_2_app, name='5', shape='v')
        self.horizontalLayout_9.addWidget(self.line_5)

        self.frame_app_btn = QtWidgets.QFrame(self.frame_2_app)
        self.frame_app_btn.setObjectName("frame_app_btn")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_app_btn)

        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")

        self.cb_app_wait = QtWidgets.QCheckBox(self.frame_app_title)
        self.cb_app_wait.setObjectName("cb_app_wait")
        self.horizontalLayout_9.addWidget(self.cb_app_wait)

        self.radiobutton_app_start = QRadioButton("START")
        self.radiobutton_app_start.setChecked(True)
        self.radiobutton_app_start.app = "START"
        # radiobutton.toggled.connect(self.onClicked)
        self.horizontalLayout_9.addWidget(self.radiobutton_app_start)

        self.radiobutton_app_stop = QRadioButton("STOP")
        self.radiobutton_app_stop.app = "STOP"
        # radiobutton.toggled.connect(self.onClicked)
        self.horizontalLayout_9.addWidget(self.radiobutton_app_stop)

        # Кнопки Application ->
        self.btn_1_app_run = UiButtonsRun(self.frame_app_btn,
                                          name='1_app',
                                          event_click=None)
        self.horizontalLayout_7.addWidget(self.btn_1_app_run)

        self.btn_2_app_view = UiButtonsViewCopy(self.frame_app_btn,
                                                name='2_app',
                                                event_click=None,
                                                type_btn='view',
                                                border_radius=(0, 0, 0, 0))
        self.horizontalLayout_7.addWidget(self.btn_2_app_view)

        self.btn_3_app_copy = UiButtonsViewCopy(self.frame_app_btn,
                                                name='3_app',
                                                event_click=None,
                                                type_btn='copy',
                                                border_radius=(0, 3, 0, 3))
        self.horizontalLayout_7.addWidget(self.btn_3_app_copy)

        self.btn_4_app_help = UiButtonsHelp(self.frame_app_btn,
                                            name='4_app',
                                            event_click=None)
        self.horizontalLayout_7.addWidget(self.btn_4_app_help)
        # <- Кнопки Application

        self.horizontalLayout_9.addWidget(self.frame_app_btn)
        self.verticalLayout.addWidget(self.frame_2_app)

        self.line_2 = UiLineFrame(self.groupbox_output, name='2', shape='h')
        self.verticalLayout.addWidget(self.line_2)

        # Область Workflow -------------------------------------------------------
        self.frame_3_wf = UiFrame(self.groupbox_output, name='3_wf', border=True)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_3_wf)

        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        self.frame_wf_title = UiFrame(self.frame_3_wf, name='wf_title', border=False)
        self.frame_wf_title.setMaximumWidth(270)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_wf_title)

        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_wf_icon = QtWidgets.QLabel(self.frame_wf_title)
        self.label_wf_icon.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_wf_icon.setText("")
        self.label_wf_icon.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/WF.png"))
        self.label_wf_icon.setObjectName("label_wf_icon")
        self.horizontalLayout_18.addWidget(self.label_wf_icon)
        self.label_wf_title = QtWidgets.QLabel(self.frame_wf_title)
        self.label_wf_title.setObjectName("label_wf_title")
        self.horizontalLayout_18.addWidget(self.label_wf_title)

        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacer_item)

        self.horizontalLayout_12.addWidget(self.frame_wf_title)

        self.line_6 = UiLineFrame(self.frame_2_app, name='6', shape='v')
        self.horizontalLayout_12.addWidget(self.line_6)

        self.frame_wf_btn = QtWidgets.QFrame(self.frame_3_wf)
        self.frame_wf_btn.setObjectName("frame_wf_btn")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_wf_btn)

        self.horizontalLayout_13.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_13.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")

        self.cb_wf_wait = QtWidgets.QCheckBox(self.frame_wf_title)
        self.cb_wf_wait.setObjectName("cb_wf_wait")
        self.horizontalLayout_12.addWidget(self.cb_wf_wait)

        # QRadioButton тест или прод
        self.radiobutton_wf_test = QRadioButton("ТЕСТ")
        self.radiobutton_wf_test.setChecked(True)
        self.radiobutton_wf_test.mode = "ТЕСТ"
        # radiobutton.toggled.connect(self.onClicked)
        self.horizontalLayout_12.addWidget(self.radiobutton_wf_test)

        self.radiobutton_wf_prod = QRadioButton("ПРОД")
        self.radiobutton_wf_prod.mode = "ПРОД"
        # radiobutton.toggled.connect(self.onClicked)
        self.horizontalLayout_12.addWidget(self.radiobutton_wf_prod)

        # Кнопки Workflow ->
        self.btn_1_wf_run = UiButtonsRun(self.frame_wf_btn,
                                         name='1_wf',
                                         event_click=None)
        self.horizontalLayout_13.addWidget(self.btn_1_wf_run)

        self.btn_2_wf_view = UiButtonsViewCopy(self.frame_wf_btn,
                                               name='2_wf',
                                               event_click=None,
                                               type_btn='view',
                                               border_radius=(0, 0, 0, 0))
        self.horizontalLayout_13.addWidget(self.btn_2_wf_view)

        self.btn_3_wf_copy = UiButtonsViewCopy(self.frame_wf_btn,
                                               name='3_wf',
                                               event_click=None,
                                               type_btn='copy',
                                               border_radius=(0, 3, 0, 3))
        self.horizontalLayout_13.addWidget(self.btn_3_wf_copy)

        self.btn_4_wf_help = UiButtonsHelp(self.frame_wf_btn,
                                           name='4_wf',
                                           event_click=None)
        self.horizontalLayout_13.addWidget(self.btn_4_wf_help)
        # <- Кнопки Workflow

        self.horizontalLayout_12.addWidget(self.frame_wf_btn)
        self.verticalLayout.addWidget(self.frame_3_wf)
        self.gridLayout.addWidget(self.groupbox_output, 2, 0, 1, 1)

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacer_item, 3, 0, 1, 1)

        self.text_edit_output_terminal = QtWidgets.QTextEdit(self.page_command)
        self.text_edit_output_terminal.setReadOnly(True)
        self.text_edit_output_terminal.setMaximumSize(QtCore.QSize(16777215, 60))
        self.text_edit_output_terminal.setObjectName("text_edit_output_terminal")
        self.gridLayout.addWidget(self.text_edit_output_terminal, 4, 0, 1, 1)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/INFA.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_command, icon3, "")
        self.page_settings = QtWidgets.QWidget()
        self.page_settings.setGeometry(QtCore.QRect(0, 0, 790, 519))
        self.page_settings.setObjectName("page_settings")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_settings)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.frame_1_settings_sql = UiFrame(self.page_settings, name='1_settings_sql', border=True)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_1_settings_sql)

        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.frame_settings_sql_title = UiFrame(self.frame_1_settings_sql, name='settings_sql_title', border=False)
        self.frame_settings_sql_title.setMinimumSize(QtCore.QSize(140, 0))
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_settings_sql_title)

        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_settings_sql_icon = QtWidgets.QLabel(self.frame_settings_sql_title)
        self.label_settings_sql_icon.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_settings_sql_icon.setText("")
        self.label_settings_sql_icon.setPixmap(
            QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/SQL.png"))
        self.label_settings_sql_icon.setObjectName("label_settings_sql_icon")
        self.horizontalLayout_19.addWidget(self.label_settings_sql_icon)
        self.label_settings_sql_title = QtWidgets.QLabel(self.frame_settings_sql_title)
        self.label_settings_sql_title.setObjectName("label_settings_sql_title")
        self.horizontalLayout_19.addWidget(self.label_settings_sql_title)
        self.horizontalLayout_11.addWidget(self.frame_settings_sql_title)

        self.frame_settings_sql_sett = UiFrame(self.frame_1_settings_sql, name='settings_sql_sett', border=False)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_settings_sql_sett)

        self.horizontalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.edit_settings_sql_path = UiLineEdit(self.frame_settings_sql_sett,
                                                 name='settings_sql_path')
        self.horizontalLayout_10.addWidget(self.edit_settings_sql_path)

        self.frame_settings_sql_btn = UiFrame(self.frame_settings_sql_sett, name='settings_sql_btn', border=False)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_settings_sql_btn)

        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.btn_settings_sql_open_dialog = UiButtonsOpenDialog(self.frame_settings_sql_btn,
                                                                name='sql',
                                                                event_click=None)
        self.gridLayout_3.addWidget(self.btn_settings_sql_open_dialog, 0, 0, 1, 1)

        self.horizontalLayout_10.addWidget(self.frame_settings_sql_btn)
        self.horizontalLayout_11.addWidget(self.frame_settings_sql_sett)
        self.verticalLayout_6.addWidget(self.frame_1_settings_sql)

        self.line_3 = UiLineFrame(self.page_settings, name='3', shape='h')
        self.verticalLayout_6.addWidget(self.line_3)

        self.frame_2_settings_infa = UiFrame(self.page_settings, name='settings_infa', border=True)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2_settings_infa)

        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.frame_1_settings_infa_path = UiFrame(self.frame_2_settings_infa, name='1_settings_infa_path', border=False)
        self.horizontalLayout_35 = QtWidgets.QHBoxLayout(self.frame_1_settings_infa_path)

        self.horizontalLayout_35.setObjectName("horizontalLayout_35")

        self.frame_settings_infa_title = UiFrame(self.frame_1_settings_infa_path, name='settings_infa_title',
                                                 border=False)
        self.frame_settings_infa_title.setMinimumSize(QtCore.QSize(128, 0))
        self.horizontalLayout_36 = QtWidgets.QHBoxLayout(self.frame_settings_infa_title)

        self.horizontalLayout_36.setObjectName("horizontalLayout_36")
        self.label_settings_infa_icon = QtWidgets.QLabel(self.frame_settings_infa_title)
        self.label_settings_infa_icon.setMaximumSize(QtCore.QSize(20, 20))
        self.label_settings_infa_icon.setText("")
        self.label_settings_infa_icon.setPixmap(
            QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/INFA.png"))
        self.label_settings_infa_icon.setScaledContents(True)
        self.label_settings_infa_icon.setWordWrap(False)
        self.label_settings_infa_icon.setObjectName("label_settings_infa_icon")
        self.horizontalLayout_36.addWidget(self.label_settings_infa_icon)
        self.label_settings_infa_title = QtWidgets.QLabel(self.frame_settings_infa_title)
        self.label_settings_infa_title.setObjectName("label_settings_infa_title")
        self.horizontalLayout_36.addWidget(self.label_settings_infa_title)
        self.horizontalLayout_35.addWidget(self.frame_settings_infa_title)

        self.frame_settings_infa_sett = UiFrame(self.frame_1_settings_infa_path, name='settings_infa_sett',
                                                border=False)
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_settings_infa_sett)

        self.horizontalLayout_37.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")

        self.edit_settings_infa_path = UiLineEdit(self.frame_settings_infa_sett,
                                                  name='settings_infa_path')
        self.horizontalLayout_37.addWidget(self.edit_settings_infa_path)

        self.frame_settings_infa_btn = UiFrame(self.frame_settings_infa_sett, name='settings_infa_btn', border=False)
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_settings_infa_btn)

        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")

        self.btn_settings_infa_open_dialog = UiButtonsOpenDialog(self.frame_settings_infa_btn,
                                                                 name='infa',
                                                                 event_click=None)
        self.gridLayout_6.addWidget(self.btn_settings_infa_open_dialog, 0, 0, 1, 1)

        self.horizontalLayout_37.addWidget(self.frame_settings_infa_btn)
        self.horizontalLayout_35.addWidget(self.frame_settings_infa_sett)
        self.verticalLayout_5.addWidget(self.frame_1_settings_infa_path)

        self.frame_2_settings_auth_test = UiFrame(self.frame_2_settings_infa, name='2_settings_auth_test', border=True)
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.frame_2_settings_auth_test)

        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_settings_auth_test_title = QtWidgets.QLabel(self.frame_2_settings_auth_test)
        self.label_settings_auth_test_title.setObjectName("label_settings_auth_test_title")
        self.horizontalLayout_38.addWidget(self.label_settings_auth_test_title)

        self.edit_settings_auth_test_user = UiLineEdit(self.frame_2_settings_auth_test,
                                                       name='settings_auth_test_user', )
        self.horizontalLayout_38.addWidget(self.edit_settings_auth_test_user)

        self.edit_settings_auth_test_password = UiLineEdit(self.frame_2_settings_auth_test,
                                                           name='settings_auth_test_password',
                                                           is_password=True)
        self.horizontalLayout_38.addWidget(self.edit_settings_auth_test_password)

        self.verticalLayout_5.addWidget(self.frame_2_settings_auth_test)

        self.frame_3_settings_auth_prod = UiFrame(self.frame_2_settings_infa, name='3_settings_auth_prod', border=True)
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.frame_3_settings_auth_prod)

        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_settings_auth_prod_title = QtWidgets.QLabel(self.frame_3_settings_auth_prod)
        self.label_settings_auth_prod_title.setObjectName("label_settings_auth_prod_title")
        self.horizontalLayout_39.addWidget(self.label_settings_auth_prod_title)

        self.edit_settings_auth_prod_user = UiLineEdit(self.frame_3_settings_auth_prod,
                                                       name='settings_auth_prod_user', )
        self.horizontalLayout_39.addWidget(self.edit_settings_auth_prod_user)

        self.edit_settings_auth_prod_password = UiLineEdit(self.frame_3_settings_auth_prod,
                                                           name='settings_auth_prod_password',
                                                           is_password=True)
        self.horizontalLayout_39.addWidget(self.edit_settings_auth_prod_password)

        self.verticalLayout_5.addWidget(self.frame_3_settings_auth_prod)
        self.verticalLayout_6.addWidget(self.frame_2_settings_infa)

        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacer_item)

        self.buttonBox_settings = QtWidgets.QDialogButtonBox(self.page_settings)
        self.buttonBox_settings.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Reset | QtWidgets.QDialogButtonBox.Save | QtWidgets.QDialogButtonBox.Help)
        self.buttonBox_settings.setObjectName("buttonBox_settings")
        self.verticalLayout_6.addWidget(self.buttonBox_settings)

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/settings.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page_settings, icon4, "")
        self.gridLayout_2.addWidget(self.toolBox, 0, 0, 1, 1)

        self._retranslate_ui()
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.update()

    def _retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_text_DMN.setText(_translate("command_infa_form", "DMN:"))
        self.lbl_text_DIS.setText(_translate("command_infa_form", "DIS:"))
        self.lbl_text_APP.setText(_translate("command_infa_form", "APP:"))
        self.lbl_text_WF.setText(_translate("command_infa_form", "WF:"))
        self.lbl_text_PS.setText(_translate("command_infa_form", "PS:"))
        self.label_sql_job_title.setText(_translate("command_infa_form", "SQL Agent Job"))
        self.cb_sql_job_wait.setText(_translate("command_infa_form", "Wait"))
        self.label_app_title.setText(_translate("command_infa_form", "Application"))
        self.cb_app_wait.setText(_translate("command_infa_form", "Wait"))
        self.label_wf_title.setText(_translate("command_infa_form", "Workflow"))
        self.cb_wf_wait.setText(_translate("command_infa_form", "Wait"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_command), _translate("command_infa_form", "Команды"))
        self.label_settings_sql_title.setText(_translate("command_infa_form", "SQL Agent Job"))
        self.edit_settings_sql_path.setPlaceholderText(self._sql_path_placeholder_text)
        self.label_settings_infa_title.setText(_translate("command_infa_form", "Informatica"))
        self.edit_settings_infa_path.setPlaceholderText(self._infa_path_placeholder_text)
        self.label_settings_auth_test_title.setText(_translate("command_infa_form", "ТЕСТ"))
        self.edit_settings_auth_test_user.setPlaceholderText(_translate("command_infa_form", "Пользователь"))
        self.edit_settings_auth_test_password.setPlaceholderText(_translate("command_infa_form", "Пароль"))
        self.label_settings_auth_prod_title.setText(_translate("command_infa_form", "ПРОД"))
        self.edit_settings_auth_prod_user.setPlaceholderText(_translate("command_infa_form", "Пользователь"))
        self.edit_settings_auth_prod_password.setPlaceholderText(_translate("command_infa_form", "Пароль"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_settings), _translate("command_infa_form", "Настройки"))

    def _load_style_ui(self):
        # Сделано чтобы одновить положение кнопок после формирования всей формы
        # Видимо формировать все стили надо делать уже после формирования всей формы и элементов на форме
        # По это костыль, в интернете не нашел решения
        self.frame_1_sql_job.set_orig_style()
        self.frame_2_app.set_orig_style()
        self.frame_3_wf.set_orig_style()

    def _load_data_ui(self):
        # ПРОВЕРКА ЗАПОЛНЕНИЯ НАСТРОЕК
        self.checking_settings()

        if not self.is_check_settings:
            self.toolBox.setCurrentIndex(self.toolBox.indexOf(self.page_settings))

        # НАСТРОЙКИ
        self.edit_settings_sql_path.setText(self.settings_cmd.get_path_sql_agent())
        self.edit_settings_infa_path.setText(self.settings_cmd.get_path_informatica())
        self.edit_settings_auth_test_user.setText(self.settings_cmd.get_user_test())
        self.edit_settings_auth_test_password.setText(self.settings_cmd.get_password_test())
        self.edit_settings_auth_prod_user.setText(self.settings_cmd.get_user_prod())
        self.edit_settings_auth_prod_password.setText(self.settings_cmd.get_password_prod())

    def _connect_events(self):
        # КНОПКИ УПАРВЛЕНИЕ КОМАНДАМИ
        self.btn_1_sql_job_view.clicked.connect(lambda: self.clicked_event_sql_job_mode(mode=self.mode.view))
        self.btn_2_sql_job_copy.clicked.connect(lambda: self.clicked_event_sql_job_mode(mode=self.mode.copy))
        self.btn_3_sql_job_help.clicked.connect(self.clicked_event_sql_job_help)

        self.btn_1_app_run.clicked.connect(lambda: self.clicked_event_app_mode(mode=self.mode.run))
        self.btn_2_app_view.clicked.connect(lambda: self.clicked_event_app_mode(mode=self.mode.view))
        self.btn_3_app_copy.clicked.connect(lambda: self.clicked_event_app_mode(mode=self.mode.copy))
        self.btn_4_app_help.clicked.connect(self.clicked_event_app_help)

        self.btn_1_wf_run.clicked.connect(lambda: self.clicked_event_wf_mode(mode=self.mode.run))
        self.btn_2_wf_view.clicked.connect(lambda: self.clicked_event_wf_mode(mode=self.mode.view))
        self.btn_3_wf_copy.clicked.connect(lambda: self.clicked_event_wf_mode(mode=self.mode.copy))
        self.btn_4_wf_help.clicked.connect(self.clicked_event_wf_help)

        # КНОПКИ ОТКРЫТИЯ ДИАЛОГА ВЫБОРА ФАЙЛА
        self.btn_settings_sql_open_dialog.clicked.connect(self.clicked_event_sql_open_dialog)
        self.btn_settings_infa_open_dialog.clicked.connect(self.clicked_event_infa_open_dialog)

        # ИЗМЕНЕНИЕ ТЕКСТОВОГО ПОЛЯ
        self.edit_settings_sql_path.textChanged.connect(self.change_event_sql_path)
        self.edit_settings_infa_path.textChanged.connect(self.change_event_infa_path)

        # КНОПКИ ОТКРЫТИЯ Informatica Administrator
        self.btn_infa_test.clicked.connect(self.clicked_event_open_informatica_monitor_test)
        self.btn_infa_prod.clicked.connect(self.clicked_event_open_informatica_monitor_prod)

        # ПАНЕЛЬ СОХРАНЕНИЯ НАСТРОЕК
        self.buttonBox_settings.accepted.connect(self.save_settings)
        self.buttonBox_settings.button(QDialogButtonBox.Reset).clicked.connect(self.clear_settings)
        self.buttonBox_settings.button(QDialogButtonBox.Help).clicked.connect(self.help_settings)
        self.buttonBox_settings.button(QDialogButtonBox.Cancel).clicked.connect(self.cancel_settings)

        # НАСТРОЙКИ
        self.edit_settings_auth_test_user.textChanged.connect(self.change_event_auth_test_user)
        self.edit_settings_auth_test_password.textChanged.connect(self.change_event_auth_test_password)
        self.edit_settings_auth_prod_user.textChanged.connect(self.change_event_auth_prod_user)
        self.edit_settings_auth_prod_password.textChanged.connect(self.change_event_auth_prod_password)

    def run_command(self, text_command, operation):
        self.text_edit_output_terminal.clear()
        if self.app.test_startapp:
            text_command = 'pwd && date'
        if text_command:
            self.text_edit_output_terminal.append(f'{operation}<-- : {text_command}')
            popen = subprocess.Popen(text_command, stdout=subprocess.PIPE, shell=True)
            for line in popen.stdout.readlines():
                self.text_edit_output_terminal.append(f'{operation}--> : {line.decode('utf-8').strip()}')
            popen.stdout.close()

    def checking_settings(self):
        self.is_check_settings = True
        if (self.settings_cmd.get_path_informatica() == ''
                or self.settings_cmd.get_path_sql_agent() == ''
                or self.settings_cmd.get_path_informatica() == ''
                or self.settings_cmd.get_user_test() == ''
                or self.settings_cmd.get_password_test() == ''
                or self.settings_cmd.get_user_prod() == ''
                or self.settings_cmd.get_password_prod() == ''):
            self.is_check_settings = False
            return None

    def change_settings_title(self, is_change=False):
        # Доступ к self и использование параметра
        if is_change:
            self.toolBox.setItemText(self.toolBox.indexOf(self.page_settings), "Настройки*")
        else:
            self.toolBox.setItemText(self.toolBox.indexOf(self.page_settings), "Настройки")

    def save_settings(self):
        self.settings_cmd.save_command()
        self.main_window.statusbar.showMessage("Настройки сохранены", 5000)
        self.change_settings_title()
        self._load_data_ui()
        # self.toolBox.setCurrentIndex(self.toolBox.indexOf(self.page_command))

    def clear_settings(self):
        self.settings_cmd.clear_command()
        self.main_window.statusbar.showMessage("Настройки очищены", 5000)
        self._load_data_ui()

    def help_settings(self):
        self.edit_settings_sql_path.setText(self._sql_path_placeholder_text)
        self.edit_settings_infa_path.setText(self._infa_path_placeholder_text)

    def cancel_settings(self):
        self._load_data_ui()

    def set_style_when_copying(self, frame):
        frame.set_copy_style()

        self.timer.timeout.connect(lambda: self._signal_timer(frame))
        self.timer.start(150)

    def _signal_timer(self, frame):
        frame.set_orig_style()
        self.timer.stop()

    def change_event_auth_test_user(self):
        self.settings_cmd.set_user_test(self.edit_settings_auth_test_user.text())

    def change_event_auth_test_password(self):
        self.settings_cmd.set_password_test(self.edit_settings_auth_test_password.text())
        self.change_settings_title(True)

    def change_event_auth_prod_user(self):
        self.settings_cmd.set_user_prod(self.edit_settings_auth_prod_user.text())
        self.change_settings_title(True)

    def change_event_auth_prod_password(self):
        self.settings_cmd.set_password_prod(self.edit_settings_auth_prod_password.text())
        self.change_settings_title(True)

    def clicked_event_sql_open_dialog(self):
        file_filter = "BAT-файл (*.bat)"
        # file_filter = "Python (*.py)"
        file_name = QFileDialog.getOpenFileName(self, caption="Открыть файл", filter=file_filter)
        if file_name:
            self.edit_settings_sql_path.setText(file_name[0])
            # self.settings_cmd.set_path_sql_agent(file_name[0])
            # self.change_settings_title(True)

    def change_event_sql_path(self):
        self.settings_cmd.set_path_sql_agent(self.edit_settings_sql_path.text())
        self.change_settings_title(True)

    def clicked_event_infa_open_dialog(self):
        file_filter = "BAT-файл (*.bat)"
        # file_filter = "Python (*.py)"
        file_name = QFileDialog.getOpenFileName(self, caption="Открыть файл", filter=file_filter)
        if file_name:
            self.edit_settings_infa_path.setText(file_name[0])
            # self.settings_cmd.set_path_informatica(file_name[0])
            # self.change_settings_title(True)

    def change_event_infa_path(self):
        self.settings_cmd.set_path_informatica(self.edit_settings_infa_path.text())
        self.change_settings_title(True)

    def clicked_event_sql_job_mode(self, mode):
        list_command = []
        for cmd in self.templates_cmd.sql_agent_job:
            if self.templates_cmd.option_path_sql_agent in cmd:
                list_command.append(
                    cmd.replace(self.templates_cmd.option_path_sql_agent, self.settings_cmd.get_path_sql_agent()))
            elif self.templates_cmd.option_dmn in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_dmn, self.edit_DMN.text()))
            elif self.templates_cmd.option_dis in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_dis, self.edit_DIS.text()))
            elif self.templates_cmd.option_app in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_app, self.edit_APP.text()))
            elif self.templates_cmd.option_wf in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_wf, self.edit_WF.text()))
            elif self.templates_cmd.option_ps in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_ps, self.edit_PS.text()))
            elif self.templates_cmd.option_wait in cmd:
                list_command.append(
                    cmd.replace(self.templates_cmd.option_wait, str(self.cb_sql_job_wait.isChecked()).lower()))
            else:
                list_command.append(cmd)

        text_command = ' '.join(list_command)

        if mode == self.mode.copy:
            pyperclip.copy(text_command)
            self.set_style_when_copying(self.frame_1_sql_job)
        else:
            dialog = UiDialogText(text=text_command, title="SQL Agent")
            dialog.setModal(True)
            dialog.exec_()

    def clicked_event_open_informatica_monitor_test(self):
        link = f'{self.settings_cmd.get_link_adm_infa_test()}#monitoring_Monitoring_admin.monitoringServicesWS/'
        webbrowser.open(link)

    def clicked_event_open_informatica_monitor_prod(self):
        link = f'{self.settings_cmd.get_link_adm_infa_prod()}#monitoring_Monitoring_admin.monitoringServicesWS/'
        webbrowser.open(link)

    @staticmethod
    def clicked_event_sql_job_help():
        webbrowser.open(
            'https://learn.microsoft.com/en-us/powershell/module/sqlserver/get-sqlagentjob?view=sqlserver-ps'
        )

    def clicked_event_app_mode(self, mode):
        list_command = []
        for cmd in self.templates_cmd.application:
            if self.templates_cmd.option_path_informatica in cmd:
                list_command.append(
                    cmd.replace(self.templates_cmd.option_path_informatica, self.settings_cmd.get_path_informatica()))
            elif self.templates_cmd.option_start_stop_app in cmd:
                if self.radiobutton_app_start.isChecked():
                    list_command.append(cmd.replace(self.templates_cmd.option_start_stop_app, "Start"))
                else:
                    list_command.append(cmd.replace(self.templates_cmd.option_start_stop_app, "Stop"))
            elif self.templates_cmd.option_user_name in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_user_name, self.settings_cmd.get_user_prod()))
            elif self.templates_cmd.option_user_pass in cmd:
                list_command.append(
                    cmd.replace(self.templates_cmd.option_user_pass, self.settings_cmd.get_password_prod()))
            elif self.templates_cmd.option_dmn in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_dmn, self.edit_DMN.text()))
            elif self.templates_cmd.option_dis in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_dis, self.edit_DIS.text()))
            elif self.templates_cmd.option_app in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_app, self.edit_APP.text()))
            elif self.templates_cmd.option_wait in cmd:
                list_command.append(
                    cmd.replace(self.templates_cmd.option_wait, str(self.cb_app_wait.isChecked()).lower()))
            else:
                list_command.append(cmd)

        text_command = ' '.join(list_command)

        if mode == self.mode.copy:
            pyperclip.copy(text_command)
            self.set_style_when_copying(self.frame_2_app)
        elif mode == self.mode.run:
            self.run_command(text_command, operation="APP")
        else:
            dialog = UiDialogText(text=text_command, title="Application")
            dialog.setModal(True)
            dialog.exec_()

    @staticmethod
    def clicked_event_app_help():
        webbrowser.open(
            'https://docs.informatica.com/data-engineering/common-content-for-data-engineering/10-4-1/command-reference/infacmd-dis-command-reference/startapplication.html')

    def clicked_event_wf_mode(self, mode):
        list_command = []
        for cmd in self.templates_cmd.workflow:
            if self.templates_cmd.option_path_informatica in cmd:
                list_command.append(
                    cmd.replace(self.templates_cmd.option_path_informatica, self.settings_cmd.get_path_informatica()))
            elif self.templates_cmd.option_dmn in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_dmn, self.edit_DMN.text()))
            elif self.templates_cmd.option_dis in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_dis, self.edit_DIS.text()))
            elif self.templates_cmd.option_app in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_app, self.edit_APP.text()))
            elif self.templates_cmd.option_wf in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_wf, self.edit_WF.text()))
            elif self.templates_cmd.option_ps in cmd:
                list_command.append(cmd.replace(self.templates_cmd.option_ps, self.edit_PS.text()))
            elif self.templates_cmd.option_user_name in cmd:
                if self.radiobutton_wf_test.isChecked():
                    list_command.append(
                        cmd.replace(self.templates_cmd.option_user_name, self.settings_cmd.get_user_test()))
                if self.radiobutton_wf_prod.isChecked():
                    list_command.append(
                        cmd.replace(self.templates_cmd.option_user_name, self.settings_cmd.get_user_prod()))
            elif self.templates_cmd.option_user_pass in cmd:
                if self.radiobutton_wf_test.isChecked():
                    list_command.append(
                        cmd.replace(self.templates_cmd.option_user_pass, self.settings_cmd.get_password_test()))
                if self.radiobutton_wf_prod.isChecked():
                    list_command.append(
                        cmd.replace(self.templates_cmd.option_user_pass, self.settings_cmd.get_password_prod()))
            elif self.templates_cmd.option_wait in cmd:
                list_command.append(
                    cmd.replace(self.templates_cmd.option_wait, str(self.cb_wf_wait.isChecked()).lower()))
            else:
                list_command.append(cmd)

        text_command = ' '.join(list_command)

        if mode == self.mode.copy:
            pyperclip.copy(text_command)
            self.set_style_when_copying(self.frame_3_wf)
        elif mode == self.mode.run:
            self.run_command(text_command, operation="WF")
        else:
            dialog = UiDialogText(text=text_command, title="Workflow")
            dialog.setModal(True)
            dialog.exec_()

    @staticmethod
    def clicked_event_wf_help():
        webbrowser.open(
            'https://docs.informatica.com/data-engineering/common-content-for-data-engineering/10-4-1/command-reference/infacmd-wfs-command-reference/startworkflow.html')
