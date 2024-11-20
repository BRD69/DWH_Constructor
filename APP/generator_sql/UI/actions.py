from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QAction, QWidget
)


class ActionTest(QAction):
    def __init__(self, parent, event_triggered=None):
        super(ActionTest, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered

        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("add_item_sql")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/add_item.png"))
        self.setText("Добавить")
        self.setStatusTip("Просто тестовая кнопка")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)


class ActionsAddItem(QAction):
    def __init__(self, parent, event_triggered=None):
        super(ActionsAddItem, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered

        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("add_item_sql")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/add_item.png"))
        self.setText("Добавить")
        self.setStatusTip("Добавить новую строку")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(lambda: self.event_triggered(None))


class ActionsDeleteItem(QAction):
    def __init__(self, parent, event_triggered=None):
        super(ActionsDeleteItem, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered

        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("delete_item_sql")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/delete_item.png"))
        self.setText("Удалить")
        self.setStatusTip("Удалить строку")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)


class ActionsClear(QAction):
    def __init__(self, parent, event_triggered=None):
        super(ActionsClear, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered

        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("clear_sql")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/clear.png"))
        self.setText("Очистить")
        self.setStatusTip("Очистить данные")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)


class ActionsFormatedText(QAction):
    def __init__(self, parent, event_triggered=None):
        super(ActionsFormatedText, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered

        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("formated_text")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/formated_text.png"))
        self.setText("Форматировать колонку")
        self.setStatusTip("Форматировать колонку. Пример: Text exampleScript -> text_example_script")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)


class ActionsTranslitColumn(QAction):
    def __init__(self, parent, event_triggered=None):
        super(ActionsTranslitColumn, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered

        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("format_translit")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/format_translit.png"))
        self.setText("Транслитерация колонки")
        self.setStatusTip("Транслитерация колонки. Пример: Текст пример -> Tekst primer")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)


class ActionsPostfixRefKey(QAction):
    def __init__(self, parent, event_triggered=None):
        super(ActionsPostfixRefKey, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered

        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("formated_ref_key")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/formated_ref_key.png"))
        self.setText("Добавить _key")
        self.setStatusTip("Добавить постфикс. Пример: link -> link_key")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)


class ActionsSQLSave(QAction):
    def __init__(self, parent, event_triggered=None):
        super(ActionsSQLSave, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered

        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("sql_save")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/sql_save.png"))
        self.setText("Формат")
        self.setStatusTip("Сохранить SQL")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)


class ActionsSQLView(QAction):
    def __init__(self, parent, event_triggered=None):
        super(ActionsSQLView, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered

        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("sql_save")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/sql_view.png"))
        self.setText("Формат")
        self.setStatusTip("Сохранить SQL")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)


class ActionsMD5View(QAction):
    def __init__(self, parent, event_triggered=None):
        super(ActionsMD5View, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered

        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("md5_view")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/md5_view.png"))
        self.setText("MD5")
        self.setStatusTip("Просмотр MD5")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)


class ActionsCopyColumn_CN_to_SN(QAction):
    def __init__(self, parent, event_triggered=None, event_hovered=None):
        super(ActionsCopyColumn_CN_to_SN, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered
        self.event_hovered = event_hovered
        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("copy_cn_sn")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/copy_cn_sn.png"))
        self.setText("CN -> SN")
        self.setStatusTip("Копировать значения column_name -> source_name")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)
        if self.event_hovered:
            self.hovered.connect(self.event_hovered)


class ActionsCopyColumn_SN_to_CN(QAction):
    def __init__(self, parent, event_triggered=None, event_hovered=None):
        super(ActionsCopyColumn_SN_to_CN, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered
        self.event_hovered = event_hovered
        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("copy_sn_cn")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/copy_sn_cn.png"))
        self.setText("SN -> CN")
        self.setStatusTip("Копировать значения source_name -> column_name")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)
        if self.event_hovered:
            self.hovered.connect(self.event_hovered)


class ActionsCopyColumn_SN_to_DES(QAction):
    def __init__(self, parent, event_triggered=None, event_hovered=None):
        super(ActionsCopyColumn_SN_to_DES, self).__init__(parent)
        self.parent = parent
        self.event_triggered = event_triggered
        self.event_hovered = event_hovered
        self._setup_ui()
        self._connect_event()

    def _setup_ui(self):
        self.setObjectName("copy_sn_des")
        self.setIcon(QIcon(":/form_sql/static/imgs/sub_form_sql/copy_sn_des.png"))
        self.setText("SN -> DES")
        self.setStatusTip("Копировать значения source_name -> description")

    def _connect_event(self):
        if self.event_triggered:
            self.triggered.connect(self.event_triggered)
        if self.event_hovered:
            self.hovered.connect(self.event_hovered)
