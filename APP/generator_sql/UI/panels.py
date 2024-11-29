from PyQt5.QtWidgets import QFrame


class UiLineFrame(QFrame):
    def __init__(self, parent=None, name='', shape=''):
        super().__init__(parent)

        self.name = name
        self.shape = shape
        self.frame_shape = QFrame.NoFrame
        if self.shape.upper() == 'V':
            self.frame_shape = QFrame.VLine
        if self.shape.upper() == 'H':
            self.frame_shape = QFrame.HLine

        self._setup_ui()

    def _setup_ui(self):
        self.setFrameShape(self.frame_shape)
        self.setFrameShadow(QFrame.Sunken)
        self.setObjectName(f"line_{self.shape.lower()}_{self.name}")


class UiFrame(QFrame):
    def __init__(self, parent=None, name='', border=False):
        super().__init__(parent)
        self.name = name
        self.border = border

        self._setup_ui()
        self._load_style_ui()

    def _setup_ui(self):
        self.setObjectName(f"frame_{self.name}")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)

    def _load_style_ui(self):
        if self.border:
            self.setStyleSheet(f"#{self.objectName()}"
                               "{\n"
                               "    border: 1px solid rgb(137, 137, 137);\n"
                               "    border-radius: 5px;\n"
                               "}")
        else:
            self.setStyleSheet(f"#{self.objectName()}"
                               "{\n"
                               "    border: none;\n"
                               "}")
        self.update()

    def set_copy_style(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           "    background-color: rgba(149, 222, 111, 128);\n"
                           "    border: 1px solid rgb(137, 137, 137);\n"
                           "    border-radius: 5px;\n"
                           "}")
        self.update()

    def set_orig_style(self):
        self._load_style_ui()
