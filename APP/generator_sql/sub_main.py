import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox, QFileDialog

from APP.generator_sql.UI.actions import *
from APP.generator_sql.UI.forms import UiDialogViewText
from APP.generator_sql.UI.tables import UiTableWidgetObject, UiTableWidgetData
from APP.generator_sql.common import get_text_null, get_length, get_state
from APP.generator_sql.core import TableSQLDataObject, TableSQLDataObjectColumn, Transliterator


class UiSQLSubForm(QWidget):
    def __init__(self, parent=None, main_window=None):
        w, h = 800, 600
        title = "Генератор SQL"
        super(UiSQLSubForm, self).__init__(parent)
        self.app = main_window.app
        self.main_window = main_window

        self.transliterator = Transliterator()

        self.sql_data_object = TableSQLDataObject(path=self.app.settings.dir_udata)

        self._title = title
        self._w = w
        self._h = h

        self._setup_ui()
        self._load_style_ui()
        self._load_tool_bar()
        self._load_data()

    def _setup_ui(self):
        self.setObjectName("SubMainWindowSQL")
        self.setMinimumSize(QtCore.QSize(self._w, self._h))
        self.setWindowTitle(self._title)

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.toolBar_GeneratorCMD = QtWidgets.QToolBar(self)
        self.toolBar_GeneratorCMD.setFixedHeight(30)
        self.toolBar_GeneratorCMD.setObjectName("toolBar_GeneratorCMD")
        # self.toolBar_GeneratorCMD.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout.addWidget(self.toolBar_GeneratorCMD)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.tableWidget_data = UiTableWidgetData(self.centralwidget, self)
        self.horizontalLayout.addWidget(self.tableWidget_data)

        self.tableWidget_object = UiTableWidgetObject(self.centralwidget, self)
        self.horizontalLayout.addWidget(self.tableWidget_object)

        self.verticalLayout.addWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(self)

    def _load_style_ui(self):
        self.toolBar_GeneratorCMD.setStyleSheet(f"#{self.toolBar_GeneratorCMD.objectName()}"
                                                "{\n"
                                                "   border: none;\n"
                                                "   border-top: 1px solid #263238;\n"
                                                "   padding: 3px;\n"
                                                "}\n"
                                                "QToolButton{\n"
                                                "   width: 25px;\n"
                                                "}\n")

    def _load_tool_bar(self):
        # self.toolBar_GeneratorCMD.addAction(ActionTest(self, self.tableWidget_data.test))
        # self.toolBar_GeneratorCMD.addSeparator()

        self.toolBar_GeneratorCMD.addAction(ActionsAddItem(self, self.tableWidget_data.add_row))
        self.toolBar_GeneratorCMD.addAction(ActionsDeleteItem(self, self.tableWidget_data.delete_row))
        self.toolBar_GeneratorCMD.addAction(ActionsClear(self, self.clear_data))
        self.toolBar_GeneratorCMD.addSeparator()
        self.toolBar_GeneratorCMD.addWidget(QLabel("Формат:"))
        self.toolBar_GeneratorCMD.addAction(ActionsFormatedText(self, self.formated_text))
        self.toolBar_GeneratorCMD.addAction(ActionsTranslitColumn(self, self.translit_rows))
        self.toolBar_GeneratorCMD.addAction(ActionsPostfixRefKey(self, self.postfix_ref_key))
        self.toolBar_GeneratorCMD.addSeparator()
        self.toolBar_GeneratorCMD.addWidget(QLabel("Копирование:"))
        self.toolBar_GeneratorCMD.addAction(ActionsCopyColumn_CN_to_SN(self, self.copy_column_name_to_source_name))
        self.toolBar_GeneratorCMD.addAction(ActionsCopyColumn_SN_to_CN(self, self.copy_source_name_to_column_name))
        self.toolBar_GeneratorCMD.addAction(ActionsCopyColumn_SN_to_DES(self, self.copy_source_name_to_description))
        self.toolBar_GeneratorCMD.addWidget(QLabel("SQL:"))
        self.toolBar_GeneratorCMD.addAction(ActionsSQLSave(self, self.sql_save))
        self.toolBar_GeneratorCMD.addAction(ActionsSQLView(self, self.sql_view))
        self.toolBar_GeneratorCMD.addSeparator()
        self.toolBar_GeneratorCMD.addWidget(QLabel("MD5:"))
        self.toolBar_GeneratorCMD.addAction(ActionsMD5View(self, self.md5_view))

    def _load_data(self):
        self.tableWidget_data.add_row(None)

    def closeEvent(self, a0):
        self.sql_data_object.save()
        self.main_window.statusbar.showMessage("Свойства и значения - сохранены", 5000)

    def clear_data(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Очистить все данные?")
        msg.setWindowTitle("Информация")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        if retval == QMessageBox.Ok:
            self.tableWidget_data.setRowCount(0)
            self.tableWidget_data.add_row(None)

    def formated_text(self):
        current_column = self.tableWidget_data.currentColumn()
        for i in range(self.tableWidget_data.rowCount()):
            item = self.tableWidget_data.item(i, current_column)
            text_new = ''
            text_orig = item.text().strip()
            for s in range(len(text_orig)):
                if s == 0:
                    text_new += text_orig[s].lower()
                elif text_orig[s] == ' ':
                    text_new = text_new + '_'
                elif text_orig[s].isupper():
                    text_new = text_new + '_' + text_orig[s].lower()
                else:
                    text_new = text_new + text_orig[s]
            text_new = text_new.replace('__', '_')
            item.setText(text_new)

    def sql_save(self):
        sql_text = self.get_sql_text()
        default_filename = f"{self.sql_data_object.get_file_name()}.sql"

        filename, _ = QFileDialog.getSaveFileName(self.main_window, "Сохранить SQL-скрипт", default_filename,
                                                  "SQL-script (*.sql);;All Files (*)")

        if filename:
            try:
                with open(filename, 'w') as file:
                    file.write(sql_text)
                self.main_window.statusbar.showMessage(f"SQL - сохранен. {filename}", 5000)
            except Exception as e:
                self.main_window.statusbar.showMessage(f"Save file error: {e}", 5000)

    def sql_view(self):
        sql_text = self.get_sql_text()
        dialog = UiDialogViewText(self, sql_text)
        dialog.setWindowTitle("Просмотр SQL")
        dialog.setModal(True)
        result = dialog.exec()
        if result == 1:
            pyperclip.copy(sql_text)
            self.main_window.statusbar.showMessage(f"SQL - скопирован", 5000)

    def get_sql_text(self):
        sql_object = self.sql_data_object
        scope = get_text_null(sql_object.scope)
        object_s = get_text_null(sql_object.object)
        source_system = get_text_null(sql_object.source_system)
        source_type = get_text_null(sql_object.source_type)
        domain = get_text_null(sql_object.domain)
        template = get_text_null(sql_object.template)
        type_s = get_text_null(sql_object.type)
        dmt_view_source = get_text_null(sql_object.dmt_view_source)
        comment = get_text_null(sql_object.comment)

        sql_text_object = (
            f"INSERT INTO [data].[object] ([scope], [object], [source_system], [source_type], [domain], [template], [type], [dmt_view_source], [comment])"
            f"\n"
            f"VALUES ({scope}, {object_s}, {source_system}, {source_type}, {domain}, {template}, {type_s}, {dmt_view_source}, {comment});")

        sql_text_object_column = f"INSERT INTO [data].[object_column] ([scope], [object], [source_system], [column_name], [data_type], [length], [precision],[scale],[is_nullable],[is_key],[default_value],[source_name],[description],[comment]) VALUES"

        for row in range(self.tableWidget_data.rowCount()):
            item = self.tableWidget_data.item(row, 0)
            item_data = item.get_sql_data_object()
            column_name = get_text_null(item_data.column_name)
            data_type = get_text_null(item_data.data_type)
            length = get_length(item_data.length)
            precision = get_text_null(item_data.precision)
            scale = get_text_null(item_data.scale)
            is_nullable = get_state(item_data.is_nullable)
            is_key = get_state(item_data.is_key)
            default_value = get_text_null(item_data.default_value)
            source_name = get_text_null(item_data.source_name)
            description = get_text_null(item_data.description)
            comment = get_text_null(item_data.comment)
            sql_text_object_column += f"\n({scope},{object_s},{source_system},{column_name},{data_type},{length},{precision},{scale},{is_nullable},{is_key},{default_value},{source_name},{description},{comment}),"

        sql_text_object_column = sql_text_object_column[:-1] + ';'
        sql_text_exec = f"EXEC [core_metadata].[exec].[create_dwh_objects] @object = '{sql_object.object}', @source_system = '{sql_object.source_system}', @scope = '{sql_object.scope}';"

        sql_text = f"{sql_text_object}\n\n{sql_text_object_column}\n\n{sql_text_exec}"
        return sql_text

    def get_md5_text(self):
        field_text = ""
        for row in range(self.tableWidget_data.rowCount()):
            item = self.tableWidget_data.item(row, 0)
            item_data = item.get_sql_data_object()
            field_text += f"{item_data.source_name}||"
        field_text = field_text[:-2]
        return f"MD5({field_text})"

    def translit_rows(self):
        try:
            current_column = self.tableWidget_data.currentColumn()
            for i in range(self.tableWidget_data.rowCount()):
                item = self.tableWidget_data.item(i, current_column)
                new_text = self.transliterator.get_tranlit(item.text())
                item.setText(new_text)
        except Exception as e:
            self.main_window.statusBar.showMessage(f"Не удалось транслитеровать текст", 5000)

    def postfix_ref_key(self):
        current_column = self.tableWidget_data.currentColumn()
        for i in range(self.tableWidget_data.rowCount()):
            item_type = self.tableWidget_data.item(i, 1)
            if item_type.text() == 'uniqueidentifier':
                item = self.tableWidget_data.item(i, current_column)
                new_text = f"{item.text()}_key"
                item.setText(new_text)

    def copy_column_name_to_source_name(self):
        sql_data_object = TableSQLDataObjectColumn()
        columns = sql_data_object.get_columns()
        input_column = columns.index("column_name")
        output_column = columns.index("source_name")

        for row in range(self.tableWidget_data.rowCount()):
            item_input = self.tableWidget_data.item(row, input_column)
            item_output = self.tableWidget_data.item(row, output_column)
            item_output.setText(item_input.text())

    def copy_source_name_to_column_name(self):
        sql_data_object = TableSQLDataObjectColumn()
        columns = sql_data_object.get_columns()
        input_column = columns.index("source_name")
        output_column = columns.index("column_name")

        for row in range(self.tableWidget_data.rowCount()):
            item_input = self.tableWidget_data.item(row, input_column)
            item_output = self.tableWidget_data.item(row, output_column)
            item_output.setText(item_input.text())

    def copy_source_name_to_description(self):
        sql_data_object = TableSQLDataObjectColumn()
        columns = sql_data_object.get_columns()
        input_column = columns.index("source_name")
        output_column = columns.index("description")

        for row in range(self.tableWidget_data.rowCount()):
            item_input = self.tableWidget_data.item(row, input_column)
            item_output = self.tableWidget_data.item(row, output_column)
            item_output.setText(item_input.text())

    def md5_view(self):
        md5_text = self.get_md5_text()
        dialog = UiDialogViewText(self, md5_text)
        dialog.setWindowTitle("Просмотр MD5")
        dialog.setModal(True)
        result = dialog.exec()
        if result == 1:
            pyperclip.copy(md5_text)
            self.main_window.statusbar.showMessage(f"MD5 - скопирован", 5000)
