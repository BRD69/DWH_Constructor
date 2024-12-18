from PyQt5 import QtWidgets, QtCore, QtGui


class UiMainWindow(QtWidgets.QMainWindow):
    class Actions:
        def __init__(self, form):
            self.form = form
            
        def close(self):
            self.form.close()
    
    def __init__(self):
        super().__init__()
        self._setup_ui()



    def _setup_ui(self):
        self.setObjectName("MainWindow")
        self.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")

        self.window_GeneratorCMD = QtWidgets.QWidget(self.mdiArea)
        self.window_GeneratorCMD.setMinimumSize(QtCore.QSize(800, 600))
        self.window_GeneratorCMD.setObjectName("window_GeneratorCMD")

        self.mdiArea.addSubWindow(self.window_GeneratorCMD)

        # self.window_GeneratorCMD.show()

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.window_GeneratorCMD)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.toolBar_GeneratorCMD = QtWidgets.QToolBar(self.window_GeneratorCMD)
        self.toolBar_GeneratorCMD.setMinimumSize(QtCore.QSize(0, 40))
        self.toolBar_GeneratorCMD.setObjectName("toolBar_GeneratorCMD")
        self.horizontalLayout.addWidget(self.toolBar_GeneratorCMD)

        self.tableWidget_data = QtWidgets.QTableWidget(self.window_GeneratorCMD)
        self.tableWidget_data.setAlternatingRowColors(True)
        self.tableWidget_data.setObjectName("tableWidget_data")
        self.tableWidget_data.setColumnCount(11)
        self.tableWidget_data.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_data.setHorizontalHeaderItem(10, item)
        self.tableWidget_data.horizontalHeader().setStretchLastSection(True)
        # self.horizontalLayout.addWidget(self.tableWidget_data)
        self.tableWidget_object = QtWidgets.QTableWidget(self.window_GeneratorCMD)
        self.tableWidget_object.setMaximumSize(QtCore.QSize(200, 16777215))
        self.tableWidget_object.setStyleSheet("#tableWidget_object{\n"
"    alternate-background-color: rgb(255, 255, 210);\n"
"    background-color: rgb(254, 255, 170);\n"
"}")
        self.tableWidget_object.setAlternatingRowColors(True)
        self.tableWidget_object.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_object.setObjectName("tableWidget_object")
        self.tableWidget_object.setColumnCount(2)
        self.tableWidget_object.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_object.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_object.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_object.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_object.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_object.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_object.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_object.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_object.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/app_img/UI/img/app/property.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        self.tableWidget_object.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/app_img/UI/img/app/value.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.tableWidget_object.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_object.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_object.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_object.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_object.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_object.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_object.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_object.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_object.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_object.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_object.setItem(7, 0, item)
        self.tableWidget_object.horizontalHeader().setVisible(True)
        self.tableWidget_object.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_object.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_object.horizontalHeader().setHighlightSections(True)
        self.tableWidget_object.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget_object.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_object.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_object.verticalHeader().setVisible(False)
        self.tableWidget_object.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget_object.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_object.verticalHeader().setStretchLastSection(False)
        # self.horizontalLayout.addWidget(self.tableWidget_object)
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)


        # self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_GeneratorCMD)

        self.action = QtWidgets.QAction(self)
        self.action.setObjectName("action")
        self.action_SQL = QtWidgets.QAction(self)
        self.action_SQL.setObjectName("action_SQL")
        self.action_DWH = QtWidgets.QAction(self)
        self.action_DWH.setObjectName("action_DWH")
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_SQL)
        self.menu_2.addAction(self.action_DWH)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "DWH App"))
        self.window_GeneratorCMD.setWindowTitle(_translate("self", "Генератор CMD"))
        item = self.tableWidget_data.verticalHeaderItem(0)
        item.setText(_translate("self", "1"))
        item = self.tableWidget_data.verticalHeaderItem(1)
        item.setText(_translate("self", "2"))
        item = self.tableWidget_data.verticalHeaderItem(2)
        item.setText(_translate("self", "3"))
        item = self.tableWidget_data.horizontalHeaderItem(0)
        item.setText(_translate("self", "column_name"))
        item = self.tableWidget_data.horizontalHeaderItem(1)
        item.setText(_translate("self", "data_type"))
        item = self.tableWidget_data.horizontalHeaderItem(2)
        item.setText(_translate("self", "length"))
        item = self.tableWidget_data.horizontalHeaderItem(3)
        item.setText(_translate("self", "precision"))
        item = self.tableWidget_data.horizontalHeaderItem(4)
        item.setText(_translate("self", "scale"))
        item = self.tableWidget_data.horizontalHeaderItem(5)
        item.setText(_translate("self", "is_nullable"))
        item = self.tableWidget_data.horizontalHeaderItem(6)
        item.setText(_translate("self", "is_key"))
        item = self.tableWidget_data.horizontalHeaderItem(7)
        item.setText(_translate("self", "default_value"))
        item = self.tableWidget_data.horizontalHeaderItem(8)
        item.setText(_translate("self", "source_name"))
        item = self.tableWidget_data.horizontalHeaderItem(9)
        item.setText(_translate("self", "description"))
        item = self.tableWidget_data.horizontalHeaderItem(10)
        item.setText(_translate("self", "comment"))
        item = self.tableWidget_object.verticalHeaderItem(0)
        item.setText(_translate("self", "scope"))
        item = self.tableWidget_object.verticalHeaderItem(1)
        item.setText(_translate("self", "object"))
        item = self.tableWidget_object.verticalHeaderItem(2)
        item.setText(_translate("self", "type"))
        item = self.tableWidget_object.verticalHeaderItem(3)
        item.setText(_translate("self", "source_system"))
        item = self.tableWidget_object.verticalHeaderItem(4)
        item.setText(_translate("self", "source_type"))
        item = self.tableWidget_object.verticalHeaderItem(5)
        item.setText(_translate("self", "domain"))
        item = self.tableWidget_object.verticalHeaderItem(6)
        item.setText(_translate("self", "template"))
        item = self.tableWidget_object.verticalHeaderItem(7)
        item.setText(_translate("self", "dmt_view_source"))
        item = self.tableWidget_object.horizontalHeaderItem(0)
        item.setText(_translate("self", "Свойство"))
        item = self.tableWidget_object.horizontalHeaderItem(1)
        item.setText(_translate("self", "Значение"))
        __sortingEnabled = self.tableWidget_object.isSortingEnabled()
        self.tableWidget_object.setSortingEnabled(False)
        item = self.tableWidget_object.item(0, 0)
        item.setText(_translate("self", "Scope"))
        item = self.tableWidget_object.item(1, 0)
        item.setText(_translate("self", "Object"))
        item = self.tableWidget_object.item(2, 0)
        item.setText(_translate("self", "Type"))
        item = self.tableWidget_object.item(3, 0)
        item.setText(_translate("self", "Source system"))
        item = self.tableWidget_object.item(4, 0)
        item.setText(_translate("self", "Source type"))
        item = self.tableWidget_object.item(5, 0)
        item.setText(_translate("self", "Domain"))
        item = self.tableWidget_object.item(6, 0)
        item.setText(_translate("self", "Template"))
        item = self.tableWidget_object.item(7, 0)
        item.setText(_translate("self", "DMT view source"))
        self.tableWidget_object.setSortingEnabled(__sortingEnabled)
        self.menu.setTitle(_translate("self", "Файл"))
        self.menu_2.setTitle(_translate("self", "Приложения"))
        self.toolBar_GeneratorCMD.setWindowTitle(_translate("self", "toolBar"))
        self.action.setText(_translate("self", "Выход"))
        self.action_SQL.setText(_translate("self", "Генератор SQL"))
        self.action_DWH.setText(_translate("self", "Генератор CMD"))
