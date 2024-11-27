import pandas
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QTableWidget

from APP.generator_sql.UI.inputs import UiComboBox, UiTableWidgetItemObject, UiTableWidgetItemObjectColumn
from APP.generator_sql.core import TableSQLDataObject, TableSQLDataObjectColumn


class UiTableWidgetObject(QTableWidget):
    def __init__(self, parent=None, main_window=None):
        super(UiTableWidgetObject, self).__init__(parent)
        self.sql_data_object = main_window.sql_data_object
        self.row_count = len(self.sql_data_object.__dict__.keys())
        self.scopes = self.sql_data_object.get_scopes()
        self.types = self.sql_data_object.get_types()

        self._setup_ui()
        self._load_style_ui()
        self._add_header()
        self._add_rows()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("tableWidget_object")
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.setRowCount(0)
        self.setColumnCount(2)
        self.setSortingEnabled(False)

        self.horizontalHeader().setVisible(True)
        self.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalHeader().setDefaultSectionSize(150)
        self.horizontalHeader().setHighlightSections(True)
        self.horizontalHeader().setMinimumSectionSize(150)
        self.horizontalHeader().setSortIndicatorShown(True)
        self.horizontalHeader().setStretchLastSection(True)

        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(23)
        self.verticalHeader().setMinimumSectionSize(23)

        self.setMaximumSize(QtCore.QSize(310, 16777215))

    def _load_style_ui(self):
        self.setStyleSheet(f"#{self.objectName()}"
                           "{\n"
                           "    alternate-background-color: rgb(255, 255, 210);\n"
                           "    background-color: rgb(254, 255, 170);\n"
                           "}\n")

    def _add_header(self):
        icon_property = QtGui.QIcon()
        icon_property.addPixmap(QtGui.QPixmap(":/form_sql/static/imgs/sub_form_sql/property.png"), QtGui.QIcon.Normal,
                                QtGui.QIcon.Off)

        icon_value = QtGui.QIcon()
        icon_value.addPixmap(QtGui.QPixmap(":/form_sql/static/imgs/sub_form_sql/value.png"), QtGui.QIcon.Normal,
                             QtGui.QIcon.Off)

        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon_property)
        item.setText("Свойство")
        self.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setIcon(icon_value)
        item.setText("Значение")
        self.setHorizontalHeaderItem(1, item)

    def _add_rows(self):
        for key in enumerate(self.sql_data_object.__dict__.keys()):
            index, name_field = key[0], key[1]
            if name_field in self.sql_data_object.get_load_value():
                row = self.rowCount()
                self.insertRow(row)

                value = self.sql_data_object.__dict__[name_field]

                item_field0 = QtWidgets.QTableWidgetItem(name_field)
                item_field0.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEnabled)
                self.setItem(row, 0, item_field0)

                if name_field == "scope":
                    combo_box = self.create_combo_box(name="scope", values=self.scopes,
                                                      name_field=name_field, row=row, column=1)
                    combo_box.set_current_index(list(self.scopes).index(value))
                    self.setCellWidget(row, 1, combo_box)
                elif name_field == "type":
                    combo_box = self.create_combo_box(name="type", values=self.types,
                                                      name_field=name_field, row=row, column=1)
                    combo_box.set_current_index(list(self.types).index(value))
                    self.setCellWidget(row, 1, combo_box)
                else:
                    item_value1 = UiTableWidgetItemObject(value=value,
                                                          name_field=name_field, row=row, column=1)
                    if name_field == "template" or name_field == "dmt_view_source":
                        item_value1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled)
                    self.setItem(row, 1, item_value1)
            else:
                continue

    def _connect_event(self):
        self.itemChanged.connect(self._change_item)

    def _change_item(self, item):
        setattr(self.sql_data_object, item.name_field, item.text())

    def create_combo_box(self, name, values, name_field, row=0, column=0):
        combo_box = UiComboBox(name=name, values=values, style='object',
                               name_field=name_field, row=row, column=column)
        combo_box.currentIndexChanged.connect(lambda: self._combo_box_current_index_change(combo_box))
        return combo_box

    def _combo_box_current_index_change(self, combo_box):
        setattr(self.sql_data_object, combo_box.name_field, combo_box.itemText(combo_box.currentIndex()))


class UiTableWidgetData(QTableWidget):
    def __init__(self, parent=None, main_window=None):
        super(UiTableWidgetData, self).__init__(parent)
        self.sub_main_window = main_window
        self.sql_data_object = TableSQLDataObjectColumn
        # self.sql_data_object_column_list = main_window.sql_data_object_column_list

        self.values_data_type = self.sql_data_object.get_values_data_type()
        self.columns = self.sql_data_object().get_columns()

        self._setup_ui()
        self._load_style_ui()
        self._add_header()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("tableWidget_data")
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        # self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setColumnCount(11)
        self.setRowCount(0)
        self.setSortingEnabled(False)
        self.horizontalHeader().setStretchLastSection(True)

    def _load_style_ui(self):
        pass

    def _add_header(self):
        for index, column in enumerate(self.columns):
            item = QtWidgets.QTableWidgetItem()
            item.setText(column)
            if column == "column_name":
                item.setBackground(QtGui.QColor(151, 183, 214))
            if column == "source_name":
                item.setBackground(QtGui.QColor(183, 159, 130))
            self.setHorizontalHeaderItem(index, item)

    def _connect_event(self):
        self.itemChanged.connect(self._change_item)
        self.itemDoubleClicked.connect(self._double_clicked)

    def _change_item(self, item: QtWidgets.QTableWidgetItem):
        name_field = item.get_name_field()

        item_0 = self.item(item.row(), 0)
        data_item_0 = item_0.sql_data_object
        if name_field in ["is_nullable", "is_key"]:
            setattr(data_item_0, name_field, item.checkState())
        # elif name_field in ["column_name"]:
        #     setattr(data_item_0, name_field, item.text())
        # elif name_field in ["data_type"]:
        #     setattr(data_item_0, name_field, item.text())
        else:
            setattr(data_item_0, name_field, item.text())

        if item.text() == '' and name_field in ["column_name", "length", "precision", "scale", "default_value", "source_name", "description"]:
            item.setBackground(QtGui.QColor(234, 255, 207))
        else:
            item.setBackground(item.get_orig_bg_color())

        # if not item.text() in self.values_data_type and name_field in ["data_type"]:
        #     item.setBackground(QtGui.QColor(255, 141, 111))
        # else:
        #     item.setBackground(item.get_orig_bg_color())

    def _double_clicked(self, item):
        if item.get_is_combo_box():
            try:
                current_index = self.sql_data_object.get_values_data_type().index(item.text())
            except ValueError:
                current_index = 0
            combo_box = UiComboBox(values=self.sql_data_object.get_values_data_type())
            combo_box.currentIndexChanged.connect(lambda: self.combo_box_changed_index(combo_box))
            combo_box.activated.connect(lambda: self.combo_box_editing_finished(combo_box))
            combo_box.set_name_field(f"data_type_{item.row()}")
            combo_box.set_row_index(item.row())
            combo_box.set_current_index(current_index)
            self.setCellWidget(item.row(), 1, combo_box)

    def keyPressEvent(self, event):
        if event.matches(QKeySequence.Paste):
            try:
                row_current, column_current, column_count = self.currentRow(), self.currentColumn(), self.columnCount()
            except Exception as e:
                self.sub_main_window.main_window.statusbar.showMessage("Выберите ячейку для вставки")
                return None

            data_clipboard = pandas.read_clipboard(sep=r'[\t]|[\n]', header=None)
            data_clipboard_list_values = data_clipboard.values.tolist()
            len_list_values = len(data_clipboard_list_values)
            rows = self.rowCount()

            if len_list_values > rows - row_current:
                _start_row = rows - row_current
                _difference = len_list_values - _start_row
                for i in range(_difference):
                    self.add_row(self.sql_data_object())

            for index, value in enumerate(data_clipboard_list_values):
                item_0 = self.item(row_current + index, 0)
                item_data = item_0.get_sql_data_object()
                if len(value) == 1:
                    item_column = self.item(row_current + index, column_current)
                    name_field = item_column.get_name_field()
                    setattr(item_data, name_field, value[0])
                    item_column.setText(value[0])
                else:
                    for index_column, value_column in enumerate(value):
                        start_index_column = column_current + index_column
                        if start_index_column > column_count - 1:
                            continue
                        item_column = self.item(row_current + index, start_index_column)
                        name_field = item_column.get_name_field()
                        setattr(item_data, name_field, value_column)
                        item_column.setText(value_column)

            self.check_data_type()

    def test(self):
        print('---test->')
        for row in range(self.rowCount()):
            item_0 = self.item(row, 0)
            sql_data_object = item_0.get_sql_data_object()
            print(sql_data_object)

    def add_row(self, sql_data_object):
        if sql_data_object is None:
            sql_data_object = self.sql_data_object()

        row = self.rowCount()
        self.insertRow(row)

        for index_col, value_col in enumerate(sql_data_object.__dict__.items()):
            if index_col == 0:
                item_0 = UiTableWidgetItemObjectColumn(value_col[1])
                item_0.set_row_index(row)
                item_0.set_name_field(value_col[0])
                item_0.set_sql_data_object(sql_data_object)
                item_0.set_orig_bg_color(item_0.background())
                self.setItem(row, index_col, item_0)
            elif value_col[0] == "data_type":
                item = UiTableWidgetItemObjectColumn(sql_data_object.data_type)
                item.set_row_index(row)
                item.set_name_field(value_col[0])
                item.set_is_combo_box(True)
                item.set_orig_bg_color(item.background())
                self.setItem(row, 1, item)
            elif value_col[0] in ["is_nullable", "is_key"]:
                item = UiTableWidgetItemObjectColumn("")
                item.set_row_index(row)
                item.set_name_field(value_col[0])
                item.setCheckState(value_col[1])
                item.set_orig_bg_color(item.background())
                self.setItem(row, index_col, item)
            else:
                item = UiTableWidgetItemObjectColumn(value_col[1])
                item.set_row_index(row)
                item.set_name_field(value_col[0])
                item.set_orig_bg_color(item.background())
                self.setItem(row, index_col, item)
        self.update()

    def delete_row(self):
        row = self.currentRow()
        self.removeRow(row)

    def check_data_type(self):
        for row in range(self.rowCount()):
            item_data_type = self.item(row, 1)
            column_field_values = self.sql_data_object.get_values_type(item_data_type.text()).__dict__
            column_indexes = self.sql_data_object().get_columns()

            for index_col, value_col in enumerate(column_indexes):
                if value_col in column_field_values.keys():
                    item = self.item(row, index_col)
                    if value_col in ["is_nullable", "is_key"]:
                        item.setCheckState(column_field_values[value_col])
                    elif value_col in ["source_name"]:
                        print(column_field_values[value_col])
                    else:
                        item.setText(column_field_values[value_col])



    def combo_box_changed_index(self, combo_box):
        row_current = combo_box.get_index_row()
        index_current = combo_box.currentIndex()
        value_current = self.sql_data_object.get_values_data_type()[index_current]
        item = self.item(row_current, 1)
        item.setText(value_current)
        self._change_item(item)

        type_str = combo_box.itemText(combo_box.currentIndex())
        column_field_values = self.sql_data_object.get_values_type(type_str).__dict__
        column_indexes = self.sql_data_object().get_columns()

        for index_col, value_col in enumerate(column_indexes):
            if value_col in column_field_values.keys():
                item = self.item(row_current, index_col)
                if value_col in ["is_nullable", "is_key"]:
                    item.setCheckState(column_field_values[value_col])
                elif value_col in ["source_name"]:
                    print(column_field_values[value_col])
                else:
                    item.setText(column_field_values[value_col])

    def combo_box_editing_finished(self, combo_box):
        self.removeCellWidget(combo_box.get_index_row(), 1)
