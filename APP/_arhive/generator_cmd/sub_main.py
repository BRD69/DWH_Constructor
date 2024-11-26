from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from APP._arhive.generator_cmd.UI.buttons import ViewButton, CopyButton
from APP._arhive.generator_cmd.UI.controls import UiGroupBox, UiHBoxLayout
from APP._arhive.generator_cmd.UI.inputs import UiLineEdit, UiLabelIcon
from APP._arhive.generator_cmd.core import StringCommand


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
        w, h = 500, 650
        title = "Команды INFA"
        super(UiSubMainWindowCommandInfa, self).__init__(parent)
        self.app = main_window.app
        self.main_window = main_window

        self._title = title
        self._w = w
        self._h = h

        self.template_commands = StringCommand(self.app.settings.dir_settings)

        self._option_dmn = self.template_commands.option_dmn
        self._option_dis = self.template_commands.option_dis
        self._option_app = self.template_commands.option_app
        self._option_wf = self.template_commands.option_wf
        self._option_ps = self.template_commands.option_ps

        # edit_start_job. Запуск JOB
        self._start_job__array = list(self.template_commands.start_job)
        self._start_job__prefix = self.template_commands.start_job_prefix
        self._start_job__index_params = {
            "_option_dmn": get_index(self._start_job__array, self._option_dmn),
            "_option_dis": get_index(self._start_job__array, self._option_dis),
            "_option_app": get_index(self._start_job__array, self._option_app),
            "_option_wf": get_index(self._start_job__array, self._option_wf),
            "_option_ps": get_index(self._start_job__array, self._option_ps),
        }
        self._start_job__position_params = {
            "_option_dmn": get_position(' '.join(self._start_job__array), self._option_dmn),
            "_option_dis": get_position(' '.join(self._start_job__array), self._option_dis),
            "_option_app": get_position(' '.join(self._start_job__array), self._option_app),
            "_option_wf": get_position(' '.join(self._start_job__array), self._option_wf),
            "_option_ps": get_position(' '.join(self._start_job__array), self._option_ps),
        }

        # edit_start_app_p
        self._start_prod_app__array = list(self.template_commands.start_prod_app)
        self._start_prod_app__prefix = self.template_commands.start_prod_app_prefix
        self._start_prod_app__index_param = {
            "_option_dmn": get_index(self._start_prod_app__array, self._option_dmn),
            "_option_dis": get_index(self._start_prod_app__array, self._option_dis),
            "_option_app": get_index(self._start_prod_app__array, self._option_app),
            "_option_wf": -1,
            "_option_ps": -1,
        }
        self._start_prod_app__position_params = {
            "_option_dmn": get_position(' '.join(self._start_prod_app__array), self._option_dmn),
            "_option_dis": get_position(' '.join(self._start_prod_app__array), self._option_dis),
            "_option_app": get_position(' '.join(self._start_prod_app__array), self._option_app),
            "_option_wf": 0,
            "_option_ps": 0,
        }

        # edit_stop_app_p
        self._stop_prod_app__array = list(self.template_commands.stop_prod_app)
        self._stop_prod_app__prefix = self.template_commands.stop_prod_app_prefix
        self._stop_prod_app__index_param = {
            "_option_dmn": get_index(self._stop_prod_app__array, self._option_dmn),
            "_option_dis": get_index(self._stop_prod_app__array, self._option_dis),
            "_option_app": get_index(self._stop_prod_app__array, self._option_app),
            "_option_wf": -1,
            "_option_ps": -1,
        }
        self._stop_prod_app__position_params = {}

        # edit_start_wf_p
        self._start_prod_wf__array = list(self.template_commands.start_prod_wf)
        self._start_prod_wf__prefix = self.template_commands.start_prod_wf_prefix
        self._start_prod_wf__index_param = {
            "_option_dmn": get_index(self._start_prod_wf__array, self._option_dmn),
            "_option_dis": get_index(self._start_prod_wf__array, self._option_dis),
            "_option_app": get_index(self._start_prod_wf__array, self._option_app),
            "_option_wf": get_index(self._start_prod_wf__array, self._option_wf),
            "_option_ps": get_index(self._start_prod_wf__array, self._option_ps),
        }
        self._start_prod_wf__position_params = {
            "_option_dmn": get_position(' '.join(self._start_prod_wf__array), self._option_dmn),
            "_option_dis": get_position(' '.join(self._start_prod_wf__array), self._option_dis),
            "_option_app": get_position(' '.join(self._start_prod_wf__array), self._option_app),
            "_option_wf": get_position(' '.join(self._start_prod_wf__array), self._option_wf),
            "_option_ps": get_position(' '.join(self._start_prod_wf__array), self._option_ps),
        }

        # edit_start_wf_t
        self._start_test_wf__array = list(self.template_commands.start_test_wf)
        self._start_test_wf__prefix = self.template_commands.start_test_wf_prefix
        self._start_test_wf__index_param = {
            "_option_dmn": get_index(self._start_test_wf__array, self._option_dmn),
            "_option_dis": get_index(self._start_test_wf__array, self._option_dis),
            "_option_app": get_index(self._start_test_wf__array, self._option_app),
            "_option_wf": get_index(self._start_test_wf__array, self._option_wf),
            "_option_ps": get_index(self._start_test_wf__array, self._option_ps),
        }
        self._start_test_wf__position_params = {}

        """ФУНКЦИИ ЗАГРУЗКИ ИНТЕРФЕЙСА И ДАННЫХ"""
        self._setup_ui()
        self._load_style_ui()
        self._load_data_ui()
        self._connect_events()

    def _setup_ui(self):
        self.setObjectName("SubMainWindowCommandInfa")
        self.setFixedSize(QtCore.QSize(self._w, self._h))
        self.setWindowTitle(self._title)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_Content = QtWidgets.QVBoxLayout()
        self.verticalLayout_Content.setObjectName("verticalLayout_Content")
        self.groupbox_input = QtWidgets.QGroupBox(self)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.groupbox_input.sizePolicy().hasHeightForWidth())
        self.groupbox_input.setSizePolicy(size_policy)
        self.groupbox_input.setStyleSheet("#groupbox_input{\n"
                                          "    border: 1px solid rgb(137, 137, 137);\n"
                                          "    border-radius: 5px;\n"
                                          "    background-color: rgb(227, 227, 227);\n"
                                          "}")
        self.groupbox_input.setObjectName("groupbox_input")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupbox_input)
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame1_DMN = QtWidgets.QFrame(self.groupbox_input)
        self.frame1_DMN.setObjectName("frame1_DMN")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame1_DMN)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.lbl_icon_DMN = UiLabelIcon(self.frame1_DMN, "icon_DMN")
        self.lbl_icon_DMN.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/DMN.png"))

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

        self.edit_DMN = UiLineEdit(self.frame1_DMN, "DMN")
        self.edit_DMN.setText("")

        self.horizontalLayout.addWidget(self.edit_DMN)
        self.verticalLayout_3.addWidget(self.frame1_DMN)
        self.frame2_DIS = QtWidgets.QFrame(self.groupbox_input)
        self.frame2_DIS.setObjectName("frame2_DIS")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame2_DIS)
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.lbl_icon_DIS = UiLabelIcon(self.frame2_DIS, "icon_DIS")
        self.lbl_icon_DIS.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/DIS.png"))

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
        self.frame3_APP = QtWidgets.QFrame(self.groupbox_input)
        self.frame3_APP.setObjectName("frame3_APP")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame3_APP)
        self.horizontalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.lbl_icon_APP = UiLabelIcon(self.frame3_APP, "icon_APP")
        self.lbl_icon_APP.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/APP.png"))

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
        self.frame4_WF = QtWidgets.QFrame(self.groupbox_input)
        self.frame4_WF.setObjectName("frame4_WF")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame4_WF)
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.lbl_icon_WF = UiLabelIcon(self.frame4_WF, "icon_WF")
        self.lbl_icon_WF.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/WF.png"))

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
        self.frame5_PS = QtWidgets.QFrame(self.groupbox_input)
        self.frame5_PS.setObjectName("frame5_PS")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame5_PS)
        self.horizontalLayout_5.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.lbl_icon_PS = UiLabelIcon(self.frame5_PS, "icon_PS")
        self.lbl_icon_PS.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/PS.png"))

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
        self.verticalLayout_Content.addWidget(self.groupbox_input)

        self.groupbox_output = QtWidgets.QGroupBox(self)
        self.groupbox_output.setStyleSheet("#groupbox_output{\n"
                                           "    border: 1px solid rgb(137, 137, 137);\n"
                                           "    border-radius: 5px;\n"
                                           "    background-color: rgb(227, 227, 227);\n"
                                           "}")
        self.groupbox_output.setObjectName("groupbox_output")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupbox_output)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupbox1_start_job = UiGroupBox(parent=self.groupbox_output,
                                              name="1_start_job", name_icon="sql", app=self.app)

        self.horizontalLayout_6 = UiHBoxLayout(self.groupbox1_start_job)

        self.lbl_icon_start_job = QtWidgets.QLabel(self.groupbox1_start_job)
        self.lbl_icon_start_job.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_job.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_job.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_job.setText("")
        self.lbl_icon_start_job.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/start"
                                                        ".png"))
        self.lbl_icon_start_job.setScaledContents(True)
        self.lbl_icon_start_job.setObjectName("lbl_icon_start_job")
        self.horizontalLayout_6.addWidget(self.lbl_icon_start_job)

        self.edit_start_job = UiLineEdit(self.groupbox1_start_job, "start_job")

        self.horizontalLayout_6.addWidget(self.edit_start_job)
        self.button_view_start_job = ViewButton(self.groupbox1_start_job,
                                                window_main=self, app=self.app,
                                                name="start_job", element=self.edit_start_job)
        self.horizontalLayout_6.addWidget(self.button_view_start_job)
        self.button_copy_start_job = CopyButton(self.groupbox1_start_job,
                                                window_main=self, app=self.app,
                                                name="start_job", element=self.edit_start_job)
        self.horizontalLayout_6.addWidget(self.button_copy_start_job)
        self.verticalLayout_4.addWidget(self.groupbox1_start_job)
        self.groupbox2_start_app_p = UiGroupBox(parent=self.groupbox_output,
                                                name="2_start_app_p", name_icon="app", app=self.app)

        self.horizontalLayout_7 = UiHBoxLayout(self.groupbox2_start_app_p)

        self.lbl_icon_start_app_p = QtWidgets.QLabel(self.groupbox2_start_app_p)
        self.lbl_icon_start_app_p.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_app_p.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_app_p.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_app_p.setText("")
        self.lbl_icon_start_app_p.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/start.png"))
        self.lbl_icon_start_app_p.setScaledContents(True)
        self.lbl_icon_start_app_p.setObjectName("lbl_icon_start_app_p")
        self.horizontalLayout_7.addWidget(self.lbl_icon_start_app_p)

        self.edit_start_app_p = UiLineEdit(self.groupbox2_start_app_p, "start_app")

        self.horizontalLayout_7.addWidget(self.edit_start_app_p)
        self.button_view_start_app_p = ViewButton(self.groupbox2_start_app_p,
                                                  window_main=self, app=self.app,
                                                  name="start_app_p", element=self.edit_start_app_p)
        self.horizontalLayout_7.addWidget(self.button_view_start_app_p)
        self.button_copy_start_app_p = CopyButton(self.groupbox2_start_app_p,
                                                  window_main=self, app=self.app,
                                                  name="start_app_p", element=self.edit_start_app_p)
        self.horizontalLayout_7.addWidget(self.button_copy_start_app_p)
        self.verticalLayout_4.addWidget(self.groupbox2_start_app_p)
        self.groupbox3_stop_app_p = UiGroupBox(parent=self.groupbox_output,
                                               name="3_stop_app_p", name_icon="app", app=self.app)

        self.horizontalLayout_8 = UiHBoxLayout(self.groupbox3_stop_app_p)

        self.lbl_icon_stop_app_p = QtWidgets.QLabel(self.groupbox3_stop_app_p)
        self.lbl_icon_stop_app_p.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_stop_app_p.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_stop_app_p.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_stop_app_p.setText("")
        self.lbl_icon_stop_app_p.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/stop.png"))
        self.lbl_icon_stop_app_p.setScaledContents(True)
        self.lbl_icon_stop_app_p.setObjectName("lbl_icon_stop_app_p")
        self.horizontalLayout_8.addWidget(self.lbl_icon_stop_app_p)

        self.edit_stop_app_p = UiLineEdit(self.groupbox3_stop_app_p, "stop_app_p")

        self.horizontalLayout_8.addWidget(self.edit_stop_app_p)
        self.button_view_stop_app_p = ViewButton(self.groupbox3_stop_app_p,
                                                 window_main=self, app=self.app,
                                                 name="stop_app_p", element=self.edit_stop_app_p)
        self.horizontalLayout_8.addWidget(self.button_view_stop_app_p)
        self.button_copy_stop_app_p = CopyButton(self.groupbox3_stop_app_p,
                                                 window_main=self, app=self.app,
                                                 name="stop_app_p", element=self.edit_stop_app_p)
        self.horizontalLayout_8.addWidget(self.button_copy_stop_app_p)
        self.verticalLayout_4.addWidget(self.groupbox3_stop_app_p)
        self.groupbox4_start_wf_p = UiGroupBox(parent=self.groupbox_output,
                                               name="4_start_wf_p", name_icon="wf", app=self.app)

        self.horizontalLayout_9 = UiHBoxLayout(self.groupbox4_start_wf_p)

        self.lbl_icon_start_wf_p = QtWidgets.QLabel(self.groupbox4_start_wf_p)
        self.lbl_icon_start_wf_p.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_wf_p.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_wf_p.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_wf_p.setText("")
        self.lbl_icon_start_wf_p.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/start.png"))
        self.lbl_icon_start_wf_p.setScaledContents(True)
        self.lbl_icon_start_wf_p.setObjectName("lbl_icon_start_wf_p")
        self.horizontalLayout_9.addWidget(self.lbl_icon_start_wf_p)

        self.edit_start_wf_p = UiLineEdit(self.groupbox4_start_wf_p, "start_wf_p")

        self.horizontalLayout_9.addWidget(self.edit_start_wf_p)
        self.button_view_start_wf_p = ViewButton(self.groupbox4_start_wf_p,
                                                 window_main=self, app=self.app,
                                                 name="start_wf_p", element=self.edit_start_wf_p)
        self.horizontalLayout_9.addWidget(self.button_view_start_wf_p)
        self.button_copy_start_wf_p = CopyButton(self.groupbox4_start_wf_p,
                                                 window_main=self, app=self.app,
                                                 name="start_wf_p", element=self.edit_start_wf_p)
        self.horizontalLayout_9.addWidget(self.button_copy_start_wf_p)
        self.verticalLayout_4.addWidget(self.groupbox4_start_wf_p)
        self.groupbox5_start_wf_t = UiGroupBox(parent=self.groupbox_output,
                                               name="5_start_wf_t", name_icon="wf", app=self.app)

        self.horizontalLayout_10 = UiHBoxLayout(self.groupbox5_start_wf_t)

        self.lbl_icon_start_wf_t = QtWidgets.QLabel(self.groupbox5_start_wf_t)
        self.lbl_icon_start_wf_t.setMinimumSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_wf_t.setMaximumSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_wf_t.setBaseSize(QtCore.QSize(16, 16))
        self.lbl_icon_start_wf_t.setText("")
        self.lbl_icon_start_wf_t.setPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/start.png"))
        self.lbl_icon_start_wf_t.setScaledContents(True)
        self.lbl_icon_start_wf_t.setObjectName("lbl_icon_start_wf_t")
        self.horizontalLayout_10.addWidget(self.lbl_icon_start_wf_t)

        self.edit_start_wf_t = UiLineEdit(self.groupbox5_start_wf_t, "start_wf_t")

        self.horizontalLayout_10.addWidget(self.edit_start_wf_t)
        self.button_view_start_wf_t = ViewButton(self.groupbox5_start_wf_t,
                                                 window_main=self, app=self.app,
                                                 name="start_wf_t", element=self.edit_start_wf_t)
        self.horizontalLayout_10.addWidget(self.button_view_start_wf_t)
        self.button_copy_start_wf_t = CopyButton(self.groupbox5_start_wf_t,
                                                 window_main=self, app=self.app,
                                                 name="start_wf_t", element=self.edit_start_wf_t)
        self.horizontalLayout_10.addWidget(self.button_copy_start_wf_t)
        self.verticalLayout_4.addWidget(self.groupbox5_start_wf_t)
        self.verticalLayout_Content.addWidget(self.groupbox_output)

        self.gridLayout.addLayout(self.verticalLayout_Content, 0, 0, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.lbl_text_DMN.setText(_translate("command_infa_form", "DMN:"))
        self.lbl_text_DIS.setText(_translate("command_infa_form", "DIS:"))
        self.lbl_text_APP.setText(_translate("command_infa_form", "APP:"))
        self.lbl_text_WF.setText(_translate("command_infa_form", "WF:"))
        self.lbl_text_PS.setText(_translate("command_infa_form", "PS:"))
        self.groupbox1_start_job.setTitle(_translate("command_infa_form", "Запуск JOB"))
        self.button_copy_start_job.setText(_translate("command_infa_form", "Copy"))
        self.groupbox2_start_app_p.setTitle(_translate("command_infa_form", "Старт APP прод"))
        self.button_copy_start_app_p.setText(_translate("command_infa_form", "Copy"))
        self.groupbox3_stop_app_p.setTitle(_translate("command_infa_form", "Стоп APP прод"))
        self.button_copy_stop_app_p.setText(_translate("command_infa_form", "Copy"))
        self.groupbox4_start_wf_p.setTitle(_translate("command_infa_form", "Старт WF прод"))
        self.button_copy_start_wf_p.setText(_translate("command_infa_form", "Copy"))
        self.groupbox5_start_wf_t.setTitle(_translate("command_infa_form", "Старт WF тест"))
        self.button_copy_start_wf_t.setText(_translate("command_infa_form", "Copy"))

    def _load_style_ui(self):
        pass

    def _load_data_ui(self):
        # ЗАГРУЖАЕМ ДАННЫЕ ПРИЛОЖЕНИЯ
        self.edit_start_job.setText(' '.join(self._start_job__array))
        self.edit_start_job.setCursorPosition(0)

        self.edit_start_app_p.setText(' '.join(self._start_prod_app__array))
        self.edit_start_app_p.setCursorPosition(0)

        self.edit_stop_app_p.setText(' '.join(self._stop_prod_app__array))
        self.edit_stop_app_p.setCursorPosition(0)

        self.edit_start_wf_p.setText(' '.join(self._start_prod_wf__array))
        self.edit_start_wf_p.setCursorPosition(0)

        self.edit_start_wf_t.setText(' '.join(self._start_test_wf__array))
        self.edit_start_wf_t.setCursorPosition(0)

        self.groupbox1_start_job.setVisible(len(self._start_job__array) > 1)
        self.groupbox2_start_app_p.setVisible(len(self._start_prod_app__array) > 1)
        self.groupbox3_stop_app_p.setVisible(len(self._stop_prod_app__array) > 1)
        self.groupbox4_start_wf_p.setVisible(len(self._start_prod_wf__array) > 1)
        self.groupbox5_start_wf_t.setVisible(len(self._start_test_wf__array) > 1)

        _count_group = int(not len(self._start_job__array) > 1) + int(not len(self._start_prod_app__array) > 1) + int(
            not len(self._stop_prod_app__array) > 1) + int(not len(self._start_prod_wf__array) > 1) + int(
            not len(self._start_test_wf__array) > 1)

        self._resize_height_window(_count_group)

    def _resize_height_window(self, count_group):
        self.setMaximumHeight(self._h - count_group * 75)

    def _connect_events(self):
        # ПОДКЛЮЧАЕМ СОБЫТИЯ К ЭЛЕМЕНТАМ ОКНА
        self.edit_DMN.textChanged.connect(self._change_edit_dmn)
        # self.edit_start_job.editingFinished.connect()

        self.edit_DIS.textChanged.connect(self._change_edit_dis)
        # self.edit_start_app_p.editingFinished.connect()

        self.edit_APP.textChanged.connect(self._change_edit_app)
        # self.edit_stop_app_p.editingFinished.connect()

        self.edit_WF.textChanged.connect(self._change_edit_wf)
        # self.edit_start_wf_p.editingFinished.connect()

        self.edit_PS.textChanged.connect(self._change_edit_ps)
        # self.edit_start_wf_t.editingFinished.connect()

    @staticmethod
    def _event_change_text(elem_in, elem_out, array, param, index_params, prefix):
        if len(array) > 1:
            array[index_params[param]] = f"{prefix[param]} {elem_in.text()}"
            elem_out.setText(' '.join(array))

    def _change_edit_dmn(self):
        # пример
        # self._start_job__array[self._start_job__index_params['_option_dmn']] = f"{self._prefix_start_job['_option_dmn']} {self.edit_DMN.text()}"
        # self.edit_START_JOB.setText(' '.join(self._start_job__array))

        elements_change = (
            {
                "elem_in": self.edit_DMN, "elem_out": self.edit_start_job,
                "array": self._start_job__array,
                "param": '_option_dmn', "index_params": self._start_job__index_params,
                "prefix": self._start_job__prefix
            },
            {
                "elem_in": self.edit_DMN, "elem_out": self.edit_start_app_p,
                "array": self._start_prod_app__array,
                "param": '_option_dmn', "index_params": self._start_prod_app__index_param,
                "prefix": self._start_prod_app__prefix
            },
            {
                "elem_in": self.edit_DMN, "elem_out": self.edit_stop_app_p,
                "array": self._stop_prod_app__array,
                "param": '_option_dmn', "index_params": self._stop_prod_app__index_param,
                "prefix": self._stop_prod_app__prefix
            },
            {
                "elem_in": self.edit_DMN, "elem_out": self.edit_start_wf_p,
                "array": self._start_prod_wf__array,
                "param": '_option_dmn', "index_params": self._start_prod_wf__index_param,
                "prefix": self._start_prod_wf__prefix
            },
            {
                "elem_in": self.edit_DMN, "elem_out": self.edit_start_wf_t,
                "array": self._start_test_wf__array,
                "param": '_option_dmn', "index_params": self._start_test_wf__index_param,
                "prefix": self._start_test_wf__prefix
            },
        )

        for elem in elements_change:
            self._event_change_text(**elem)

    def _change_edit_dis(self):
        elements_change = (
            {
                "elem_in": self.edit_DIS, "elem_out": self.edit_start_job,
                "array": self._start_job__array,
                "param": '_option_dis', "index_params": self._start_job__index_params,
                "prefix": self._start_job__prefix
            },
            {
                "elem_in": self.edit_DIS, "elem_out": self.edit_start_app_p,
                "array": self._start_prod_app__array,
                "param": '_option_dis', "index_params": self._start_prod_app__index_param,
                "prefix": self._start_prod_app__prefix
            },
            {
                "elem_in": self.edit_DIS, "elem_out": self.edit_stop_app_p,
                "array": self._stop_prod_app__array,
                "param": '_option_dis', "index_params": self._stop_prod_app__index_param,
                "prefix": self._stop_prod_app__prefix
            },
            {
                "elem_in": self.edit_DIS, "elem_out": self.edit_start_wf_p,
                "array": self._start_prod_wf__array,
                "param": '_option_dis', "index_params": self._start_prod_wf__index_param,
                "prefix": self._start_prod_wf__prefix
            },
            {
                "elem_in": self.edit_DIS, "elem_out": self.edit_start_wf_t,
                "array": self._start_test_wf__array,
                "param": '_option_dis', "index_params": self._start_test_wf__index_param,
                "prefix": self._start_test_wf__prefix
            },
        )

        for elem in elements_change:
            self._event_change_text(**elem)

    def _change_edit_app(self):
        elements_change = (
            {
                "elem_in": self.edit_APP, "elem_out": self.edit_start_job,
                "array": self._start_job__array,
                "param": '_option_app', "index_params": self._start_job__index_params,
                "prefix": self._start_job__prefix
            },
            {
                "elem_in": self.edit_APP, "elem_out": self.edit_start_app_p,
                "array": self._start_prod_app__array,
                "param": '_option_app', "index_params": self._start_prod_app__index_param,
                "prefix": self._start_prod_app__prefix
            },
            {
                "elem_in": self.edit_APP, "elem_out": self.edit_stop_app_p,
                "array": self._stop_prod_app__array,
                "param": '_option_app', "index_params": self._stop_prod_app__index_param,
                "prefix": self._stop_prod_app__prefix
            },
            {
                "elem_in": self.edit_APP, "elem_out": self.edit_start_wf_p,
                "array": self._start_prod_wf__array,
                "param": '_option_app', "index_params": self._start_prod_wf__index_param,
                "prefix": self._start_prod_wf__prefix
            },
            {
                "elem_in": self.edit_APP, "elem_out": self.edit_start_wf_t,
                "array": self._start_test_wf__array,
                "param": '_option_app', "index_params": self._start_test_wf__index_param,
                "prefix": self._start_test_wf__prefix
            },
        )

        for elem in elements_change:
            self._event_change_text(**elem)

    def _change_edit_wf(self):
        elements_change = (
            {
                "elem_in": self.edit_WF, "elem_out": self.edit_start_job,
                "array": self._start_job__array,
                "param": '_option_wf', "index_params": self._start_job__index_params,
                "prefix": self._start_job__prefix
            },
            {
                "elem_in": self.edit_WF, "elem_out": self.edit_start_wf_p,
                "array": self._start_prod_wf__array,
                "param": '_option_wf', "index_params": self._start_prod_wf__index_param,
                "prefix": self._start_prod_wf__prefix
            },
            {
                "elem_in": self.edit_WF, "elem_out": self.edit_start_wf_t,
                "array": self._start_test_wf__array,
                "param": '_option_wf', "index_params": self._start_test_wf__index_param,
                "prefix": self._start_test_wf__prefix
            },
        )

        for elem in elements_change:
            self._event_change_text(**elem)

    def _change_edit_ps(self):
        elements_change = (
            {
                "elem_in": self.edit_PS, "elem_out": self.edit_start_job,
                "array": self._start_job__array,
                "param": '_option_ps', "index_params": self._start_job__index_params,
                "prefix": self._start_job__prefix
            },
            {
                "elem_in": self.edit_PS, "elem_out": self.edit_start_wf_p,
                "array": self._start_prod_wf__array,
                "param": '_option_ps', "index_params": self._start_prod_wf__index_param,
                "prefix": self._start_prod_wf__prefix
            },
            {
                "elem_in": self.edit_PS, "elem_out": self.edit_start_wf_t,
                "array": self._start_test_wf__array,
                "param": '_option_ps', "index_params": self._start_test_wf__index_param,
                "prefix": self._start_test_wf__prefix
            },
        )

        for elem in elements_change:
            self._event_change_text(**elem)
