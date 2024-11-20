from PyQt5 import QtWidgets, QtCore


class UiDialogViewText(QtWidgets.QDialog):
    def __init__(self, parent=None, text=""):
        super(UiDialogViewText, self).__init__(parent)
        self.text = text
        self._setup_ui()
        self._load_data()

    def _setup_ui(self):
        self.setObjectName("DialogViewSQL")
        self.setWindowTitle("SQL")
        self.resize(600, 350)
        self.setBaseSize(QtCore.QSize(600, 350))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.buttonBox.accepted.connect(self.accept)  # type: ignore
        self.buttonBox.rejected.connect(self.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def _load_data(self):
        self.textEdit.setText(self.text)
