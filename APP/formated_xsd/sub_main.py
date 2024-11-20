import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from APP.formated_xsd.core import remove_annotations


class UiFormatedXSDForm(QWidget):
    def __init__(self, parent=None, main_window=None):
        w, h = 900, 700
        title = "Форматировать XSD"

        super(UiFormatedXSDForm, self).__init__(parent)
        self.app = main_window.app
        self.main_window = main_window

        self.path_tmp = self.app.settings.dir_tmp
        self.file_name_xml_input = os.path.join(self.path_tmp, '_input.xml')
        self.file_name_xml_output = os.path.join(self.path_tmp, '_output.xml')

        self._title = title
        self._w = w
        self._h = h

        self._setup_ui()
        self._connect_events()

    def _setup_ui(self):
        self.setObjectName("SubMainFormatedXSDForm")
        self.setMinimumSize(QtCore.QSize(self._w, self._h))
        self.setWindowTitle(self._title)
        self.showMaximized()

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.groupBox_input = QtWidgets.QGroupBox(self)
        self.groupBox_input.setObjectName("groupBox_input")
        self.groupBox_input.setTitle("Исходный XSD")

        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_input)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit_input = QtWidgets.QTextEdit(self.groupBox_input)
        self.textEdit_input.setObjectName("textEdit_input")
        self.gridLayout.addWidget(self.textEdit_input, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_input)
        self.btn_formated = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_formated.sizePolicy().hasHeightForWidth())
        self.btn_formated.setSizePolicy(sizePolicy)
        self.btn_formated.setMinimumSize(QtCore.QSize(20, 100))
        self.btn_formated.setMaximumSize(QtCore.QSize(50, 100))
        self.btn_formated.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/form_command_infa/static/imgs/sub_form_command_infa/start.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_formated.setIcon(icon)
        self.btn_formated.setIconSize(QtCore.QSize(20, 20))
        self.btn_formated.setObjectName("btn_formated")
        self.horizontalLayout.addWidget(self.btn_formated)

        self.groupBox_output = QtWidgets.QGroupBox(self)
        self.groupBox_output.setObjectName("groupBox_output")
        self.groupBox_output.setTitle("Обработанный XSD")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_output)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_output = QtWidgets.QTextEdit(self.groupBox_output)
        self.textEdit_output.setObjectName("textEdit_output")
        self.gridLayout_2.addWidget(self.textEdit_output, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_output)

        QtCore.QMetaObject.connectSlotsByName(self)

    def _connect_events(self):
        self.btn_formated.clicked.connect(self.formated_xsd_text)

    def formated_xsd_text(self):
        input_text = self.textEdit_input.toPlainText()
        file_input = open(self.file_name_xml_input, 'w')
        file_input.write(input_text.strip())
        file_input.close()

        answer = remove_annotations(self.file_name_xml_input, self.file_name_xml_output)

        if answer["error"]:
            self.textEdit_output.setText(answer["text_error"])
        else:
            file_output = open(self.file_name_xml_output, 'r')
            file_output_text = file_output.read()
            self.textEdit_output.setText(file_output_text)
            file_output.close()




