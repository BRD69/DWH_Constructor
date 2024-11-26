from PyQt5 import QtCore, QtGui, QtWidgets


class UiDialogText(QtWidgets.QDialog):
    def __init__(self, text, title):
        h, w = 100, 750
        super(UiDialogText, self).__init__()

        self.size = QtCore.QSize(w, h)
        self.text = text
        self.title = title

        self._setup_ui()

        self._set_data()

    def _setup_ui(self):
        self.setObjectName("DialogText")
        self.resize(self.size)

        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self._retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("DialogText", "Команда INFA"))

    def _set_data(self):
        self.textEdit.setText(self.text)
        self.setWindowTitle(f"{self.title}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = UiDialogText("")
    ui.show()
    sys.exit(app.exec_())
