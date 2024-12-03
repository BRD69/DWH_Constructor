import pyperclip
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog

from APP.generator_sql.UI.buttons import UiButtonsTest, UiButtonsSave, UiButtonsRun, UiButtonsCopy
from APP.generator_sql.UI.inputs import UiLineEdit, UiTextEdit
from APP.generator_sql.UI.panels import UiFrame, UiLineFrame
from APP.generator_sql.core import SQLConnect


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


class UiDialogSQLRun(QtWidgets.QDialog):
    def __init__(self, parent=None, sql_query="", main_window=None, sql_data_object=None):
        super(UiDialogSQLRun, self).__init__(parent)

        self.app = main_window.app
        self.main_window = main_window
        self.sql_data_object = sql_data_object
        self.sql_connect = SQLConnect(path=self.app.settings.dir_udata)
        self.sql_query = sql_query
        self.sql_connect_status = False

        self._setup_ui()
        self._load_style_ui()
        self._load_data()
        self._connect_events()

    def _setup_ui(self):
        self.setObjectName("DialogSQLRun")
        self.resize(800, 600)
        self.setWindowTitle("SQL Выполнить")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.frame_1_top = UiFrame(self, name='1_top', border=False)

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_1_top)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.frame_1_connect = UiFrame(self, name='1_connect', border=True)
        self.frame_1_connect.setMinimumWidth(300)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_1_connect)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")

        self.frame_1_server = UiFrame(self, name='1_server', border=False)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_1_server)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_server = QtWidgets.QLabel(self.frame_1_server)
        self.label_server.setText("Сервер:")
        self.label_server.setObjectName("label_server")
        self.horizontalLayout.addWidget(self.label_server)

        self.edit_server = UiLineEdit(self.frame_1_server, "server")

        self.horizontalLayout.addWidget(self.edit_server)
        self.verticalLayout.addWidget(self.frame_1_server)

        self.line_1_h = UiLineFrame(self.frame_1_connect, name='1H', shape='H')
        self.verticalLayout.addWidget(self.line_1_h)

        self.frame_2_db = UiFrame(self, name='2_db', border=False)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2_db)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_db = QtWidgets.QLabel(self.frame_2_db)
        self.label_db.setText("База данных:")
        self.label_db.setObjectName("label_db")
        self.horizontalLayout_2.addWidget(self.label_db)

        self.edit_db = UiLineEdit(self.frame_2_db, "db")

        self.horizontalLayout_2.addWidget(self.edit_db)
        self.verticalLayout.addWidget(self.frame_2_db)

        self.line_2_h = UiLineFrame(self.frame_1_connect, name='1H', shape='H')
        self.verticalLayout.addWidget(self.line_2_h)

        self.frame_3_auth = UiFrame(self, name='3_auth', border=False)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3_auth)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.checkBox_auth = QtWidgets.QCheckBox(self.frame_3_auth)
        self.checkBox_auth.setText("Аунтификация Windows")
        self.checkBox_auth.setChecked(True)
        self.checkBox_auth.setEnabled(False)
        self.checkBox_auth.setObjectName("checkBox_auth")

        self.horizontalLayout_3.addWidget(self.checkBox_auth)
        self.verticalLayout.addWidget(self.frame_3_auth)

        self.line_3_h = UiLineFrame(self.frame_1_connect, name='3H', shape='H')
        self.verticalLayout.addWidget(self.line_3_h)

        self.frame_4_driver = UiFrame(self, name='4_driver', border=False)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4_driver)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_driver = QtWidgets.QLabel(self.frame_4_driver)
        self.label_driver.setText("Драйвер:")
        self.label_driver.setEnabled(False)
        self.label_driver.setObjectName("label_driver")
        self.horizontalLayout_4.addWidget(self.label_driver)

        self.edit_driver = UiLineEdit(self.frame_4_driver, "driver")
        self.edit_driver.setText("ODBC Driver 17 for SQL Server")
        self.edit_driver.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.edit_driver)
        self.verticalLayout.addWidget(self.frame_4_driver)

        self.line_4_h = UiLineFrame(self.frame_1_connect, name='4H', shape='H')
        self.verticalLayout.addWidget(self.line_4_h)

        self.frame_5_btn = UiFrame(self, name='5_btn', border=False)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5_btn)
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.label_status = QtWidgets.QLabel(self.frame_5_btn)
        self.label_status.setMaximumSize(QtCore.QSize(25, 25))
        self.label_status.setText("")
        self.label_status.setScaledContents(True)
        self.label_status.setObjectName("label_status")
        self.horizontalLayout_5.addWidget(self.label_status)

        self.btn_test = UiButtonsTest(self.frame_5_btn, name='test')
        self.horizontalLayout_5.addWidget(self.btn_test)

        spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacer_item)

        self.btn_save = UiButtonsSave(self, name='save')

        self.horizontalLayout_5.addWidget(self.btn_save)
        self.verticalLayout.addWidget(self.frame_5_btn)
        self.horizontalLayout_11.addWidget(self.frame_1_connect)

        self.line_6_v = UiLineFrame(self.frame_1_connect, name='6V', shape='V')
        self.horizontalLayout_11.addWidget(self.line_6_v)

        self.frame_2_query = UiFrame(self.frame_1_top, name="2_query", border=True)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2_query)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.text_edit_query = UiTextEdit(self.frame_2_query, name='query', read_only=False)
        self.verticalLayout_3.addWidget(self.text_edit_query)

        self.frame_query_btn = UiFrame(self.frame_2_query, name='query_btn', border=False)

        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_query_btn)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")

        spacer_item_1 = QtWidgets.QSpacerItem(991, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacer_item_1)

        self.btn_run = UiButtonsRun(self.frame_query_btn, name='run')
        self.horizontalLayout_12.addWidget(self.btn_run)

        self.verticalLayout_3.addWidget(self.frame_query_btn)
        self.horizontalLayout_11.addWidget(self.frame_2_query)
        self.verticalLayout_5.addWidget(self.frame_1_top)

        self.line_7_h = UiLineFrame(self.frame_1_connect, name='7_h', shape='H')
        self.verticalLayout_5.addWidget(self.line_7_h)

        self.frame_2_result = UiFrame(self.frame_1_top, name="2_result", border=True)

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2_result)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.text_edit_result = UiTextEdit(self.frame_2_result, name='result', read_only=True)
        self.verticalLayout_4.addWidget(self.text_edit_result)

        self.frame_result_btn = UiFrame(self.frame_2_result, name='result_btn', border=False)

        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_result_btn)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")

        spacer_item_2 = QtWidgets.QSpacerItem(1088, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacer_item_2)

        self.btn_result_save = UiButtonsSave(self, name='save')
        self.horizontalLayout_13.addWidget(self.btn_result_save)

        self.btn_result_copy = UiButtonsCopy(self, name='copy')

        self.horizontalLayout_13.addWidget(self.btn_result_copy)
        self.verticalLayout_4.addWidget(self.frame_result_btn)
        self.verticalLayout_5.addWidget(self.frame_2_result)

        QtCore.QMetaObject.connectSlotsByName(self)

    def _load_style_ui(self):
        self.active_connect_icon = QtGui.QPixmap(":/form_sql/static/imgs/sub_form_sql/active_connect.png")
        self.no_connect_icon = QtGui.QPixmap(":/form_sql/static/imgs/sub_form_sql/no_connect.png")

    def _load_data(self):
        self.text_edit_result.clear()

        # ДАННЫЕ ДЛЯ ПОДКЛЮЧЕНИЯ
        self.edit_server.setText(self.sql_connect.server)
        self.edit_db.setText(self.sql_connect.database)
        self.checkBox_auth.setChecked(self.sql_connect.get_bool_trusted_connection(self.sql_connect.trusted_connection))
        self.edit_driver.setText(self.sql_connect.driver)

        # ЗАПРОС ДЛЯ ВЫПОЛНЕНИЯ
        self.text_edit_query.setText(self.sql_query)

        # ПРОВЕРКА ПОДКЛЮЧЕНИЯ К БД
        self.clicked_event_btn_test_connect()

    def _connect_events(self):
        self.edit_server.textChanged.connect(self.change_event_edit_server)
        self.edit_db.textChanged.connect(self.change_event_edit_db)

        self.text_edit_query.textChanged.connect(self.change_event_text_query)

        self.btn_test.clicked.connect(self.clicked_event_btn_test_connect)
        self.btn_save.clicked.connect(self.clicked_event_btn_save_sql)
        self.btn_run.clicked.connect(self.clicked_event_btn_run)
        self.btn_result_save.clicked.connect(self.clicked_event_btn_result_save)
        self.btn_result_copy.clicked.connect(self.clicked_event_btn_result_copy)

    def set_connect_status(self, status=False):
        self.sql_connect_status = status
        if self.sql_connect_status:
            self.label_status.setPixmap(self.active_connect_icon)
            self.btn_run.setEnabled(True)
        else:
            self.label_status.setPixmap(self.no_connect_icon)
            self.btn_run.setEnabled(False)

    def change_event_edit_server(self):
        self.sql_connect.set_server(self.edit_server.text())

    def change_event_edit_db(self):
        self.sql_connect.set_database(self.edit_db.text())

    def change_event_text_query(self):
        self.sql_query = self.text_edit_query.toPlainText()

    def clicked_event_btn_test_connect(self):
        self.set_connect_status(False)
        if self.app.settings.platform in self.app.settings.Platforms.windows:
            import pyodbc
            # Настройки подключения
            server = self.sql_connect.server  # Имя сервера и экземпляр SQL Server
            database = self.sql_connect.database  # Имя базы данных
            trusted_connection = self.sql_connect.trusted_connection  # Используем доверительное подключение (доменная аутентификация)
            driver = self.sql_connect.driver
            if server and database and trusted_connection and driver:
                try:
                    connection_string = f'DRIVER={driver};' \
                                        f'SERVER={server};' \
                                        f'DATABASE={database};' \
                                        f'Trusted_Connection={trusted_connection};'

                    conn = pyodbc.connect(connection_string)
                    cursor = conn.cursor()

                    # Выполняем простой запрос для проверки соединения
                    cursor.execute("SELECT 1;")
                    result = cursor.fetchone()

                    if result is not None:
                        self.set_connect_status(True)
                except Exception as e:
                    self.label_status.setPixmap(self.no_connect_icon)
                    print(e)
                finally:
                    if conn:
                        conn.close()

    def clicked_event_btn_save_sql(self):
        self.sql_connect.save()
        self.main_window.statusbar.showMessage("SQL данные сохранены", 5000)

    def clicked_event_btn_run(self):
        self.text_edit_result.clear()

        if self.app.settings.platform in self.app.settings.Platforms.windows:
            import pyodbc
            # Настройки подключения
            server = self.sql_connect.server  # Имя сервера и экземпляр SQL Server
            database = self.sql_connect.database  # Имя базы данных
            trusted_connection = self.sql_connect.trusted_connection  # Используем доверительное подключение (доменная аутентификация)
            driver = self.sql_connect.driver

            # Строка подключения
            connection_string = f'DRIVER={driver};' \
                                f'SERVER={server};' \
                                f'DATABASE={database};' \
                                f'Trusted_Connection={trusted_connection};'

            # Устанавливаем соединение
            conn = pyodbc.connect(connection_string)

            # Выполняем SQL-запрос
            cursor = conn.cursor()

            try:
                result = cursor.execute(self.sql_query.strip())
                conn.commit()  # Фиксируем изменения
                for mes in result.messages:
                    if len(mes) > 1:
                        text = mes[1].replace('[Microsoft][ODBC SQL Server Driver][SQL Server]', '')
                        self.text_edit_result.append(text.strip())
                self.main_window.statusbar.showMessage("Запрос выполнен", 5000)

            except Exception as e:
                conn.rollback()  # Отменяем изменения при ошибке
                self.text_edit_result.setText(f"Произошла ошибка: {e}")
            finally:
                cursor.close()
                conn.close()

    def clicked_event_btn_result_save(self):
        sql_text = self.text_edit_result.toPlainText()
        default_filename = f"EXEC_{self.sql_data_object.get_file_name()}.sql"

        filename, _ = QFileDialog.getSaveFileName(self.main_window, "Сохранить SQL-скрипт", default_filename,
                                                  "SQL-script (*.sql);;All Files (*)")

        if filename:
            try:
                with open(filename, 'w') as file:
                    file.write(sql_text)
                self.main_window.statusbar.showMessage(f"SQL - сохранен. {filename}", 5000)
            except Exception as e:
                self.main_window.statusbar.showMessage(f"Save file error: {e}", 5000)

    def clicked_event_btn_result_copy(self):
        pyperclip.copy(self.text_edit_result.toPlainText())

