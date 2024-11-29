from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QComboBox, QTableWidgetItem, QLineEdit, QSizePolicy, QTextEdit


class UiTableWidgetItemObject(QTableWidgetItem):
    def __init__(self, value, name_field=None, row=0, column=0):
        super().__init__(value)
        self.name_field = name_field
        self.row = row
        self.column = column


class UiTableWidgetItemObjectColumn(QTableWidgetItem):
    def __init__(self, value):
        super().__init__(value)
        self.sql_data_object = None
        self.name_field = ''
        self.row_index = 0
        self.is_combo_box = False
        self.combo_box = None
        self.orig_bg_color = None

    def set_row_index(self, row_index):
        self.row_index = row_index

    def get_row_index(self):
        return self.row_index

    def set_sql_data_object(self, sql_data_object):
        self.sql_data_object = sql_data_object

    def get_sql_data_object(self):
        return self.sql_data_object

    def set_name_field(self, name_field):
        self.name_field = name_field

    def get_name_field(self):
        return self.name_field

    def set_is_combo_box(self, is_combo_box):
        self.is_combo_box = is_combo_box

    def get_is_combo_box(self):
        return self.is_combo_box

    def set_combo_box(self, combo_box):
        self.combo_box = combo_box
        self.set_is_combo_box(True)

    def get_combo_box(self):
        return self.combo_box

    def set_orig_bg_color(self, orig_bg_color):
        self.orig_bg_color = orig_bg_color

    def get_orig_bg_color(self):
        return self.orig_bg_color


class UiComboBox(QComboBox):
    def __init__(self, name='', values=(), style=None, name_field=None,
                 row=0, column=0, event_changed_index=None):
        super(UiComboBox, self).__init__()

        self.name = f'combo_box_{name}'
        self.event_changed_index = event_changed_index
        self.name_field = name_field
        # self.row = row
        self.column = column

        self.values = tuple(values)
        self.style = style
        self.index_row = 0

        self._setup_ui()
        self._load_style_ui()
        self._load_data_ui()

    def _setup_ui(self):
        self.setObjectName(self.name)

    def _load_style_ui(self):
        if self.style is None:
            self.setStyleSheet("QComboBox"
                               "{\n"
                               "    border: 0px solid rgb(204, 204, 204);\n"
                               "}\n"
                               "QComboBox::drop-down"
                               "{\n"
                               "    border:0;\n"
                               "}\n"
                               "QComboBox::down-arrow"
                               "{\n"
                               "    image: url(:/form_sql/static/imgs/sub_form_sql/expand_more.png);\n"
                               "    width: 20px;\n"
                               "    height: 20px;\n"
                               "    margin-right: 10px;\n"
                               "}\n"
                               "QComboBox:on{\n"
                               "    background-color: none;\n"
                               "}\n"
                               "QListView"
                               "{\n"
                               "    selection-color: rgb(0, 0, 0);\n"
                               "    font-size: 14px;\n"
                               "    outline: 0;\n"
                               "    padding: 5px;\n"
                               "}\n")
        else:
            self.setStyleSheet(f"QComboBox"
                               "{\n"
                               "    background-color: rgb(254, 255, 170);\n"
                               "    border: 0px solid rgb(204, 204, 204);\n"
                               "}\n"
                               f"QComboBox::drop-down"
                               "{\n"
                               "    border:0;\n"
                               "}\n"
                               f"QComboBox::down-arrow"
                               "{\n"
                               "    image: url(:/form_sql/static/imgs/sub_form_sql/expand_more.png);\n"
                               "    width: 20px;\n"
                               "    height: 20px;\n"
                               "    margin-right: 10px;\n"
                               "}\n"
                               f"QComboBox:on"
                               "{\n"
                               "    background-color: none;\n"
                               "}\n"
                               f"QListView"
                               "{\n"
                               "    background-color: rgba(236, 236, 236, 128);\n"
                               "    selection-color: rgb(0, 0, 0);\n"
                               "    font-size: 14px;\n"
                               "    outline: 0;\n"
                               "    padding: 5px;\n"
                               "}\n")

    def _load_data_ui(self):
        for index, value in enumerate(self.values):
            self.addItem(value)
            self.setItemData(index + 1, value)

    def set_name_field(self, name_field):
        self.name_field = name_field

    def set_current_index(self, current_index):
        self.setCurrentIndex(current_index)

    def set_row_index(self, index_row):
        self.index_row = index_row

    def get_index_row(self):
        return self.index_row

    def set_visible(self, visible):
        self.setVisible(visible)


class UiLineEdit(QLineEdit):
    def __init__(self, parent=None, name=None, read_only=False, is_password=False, key_option=''):
        super(UiLineEdit, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.key_option = key_option
        self.read_only = read_only
        self.is_password = is_password
        self._height = 24

        self._setup_ui()
        self._load_style_ui()

    def _setup_ui(self):
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())

        self.setObjectName(f"edit_{self.name}")
        self.setMinimumSize(QSize(0, self._height))
        self.setMaximumSize(QSize(16777215, self._height))
        self.setSizePolicy(size_policy)
        self.setReadOnly(self.read_only)
        if self.is_password:
            self.setEchoMode(QLineEdit.Password)

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           "    padding-left:3px;\n"
                           "    border: 1px solid rgb(180, 180, 180);\n"
                           "    border-radius: 3px;\n"
                           "}\n")


class UiTextEdit(QTextEdit):
    def __init__(self, parent=None, name=None, read_only=False):
        super(UiTextEdit, self).__init__(parent)
        self.parent = parent
        self.name = name
        self.read_only = read_only

        self._setup_ui()
        self._load_style_ui()

    def _setup_ui(self):
        self.setObjectName(f"text_edit_{self.name}")
        self.setReadOnly(self.read_only)

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           "    border: 1px solid rgb(180, 180, 180);\n"
                           "    border-radius: 5px;\n"
                           "    background-color: rgb(243, 243, 243);\n"
                           "}")
