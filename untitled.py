# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1126, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.style_trigger_pb = QtWidgets.QPushButton(self.centralwidget)
        self.style_trigger_pb.setObjectName("style_trigger_pb")
        self.horizontalLayout_2.addWidget(self.style_trigger_pb)
        self.table_trigger_pb = QtWidgets.QPushButton(self.centralwidget)
        self.table_trigger_pb.setObjectName("table_trigger_pb")
        self.horizontalLayout_2.addWidget(self.table_trigger_pb)
        self.text_trigger_pb = QtWidgets.QPushButton(self.centralwidget)
        self.text_trigger_pb.setObjectName("text_trigger_pb")
        self.horizontalLayout_2.addWidget(self.text_trigger_pb)
        self.clear_text_pb = QtWidgets.QPushButton(self.centralwidget)
        self.clear_text_pb.setObjectName("clear_text_pb")
        self.horizontalLayout_2.addWidget(self.clear_text_pb)
        self.add_text_pb = QtWidgets.QPushButton(self.centralwidget)
        self.add_text_pb.setObjectName("add_text_pb")
        self.horizontalLayout_2.addWidget(self.add_text_pb)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_3.setObjectName("horizontalWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.horizontalWidget_3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalLayout_3.addWidget(self.textEdit_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_5.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalWidget_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_5.addWidget(self.pushButton_10)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addWidget(self.horizontalWidget_3)
        self.horizontalWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_4.setObjectName("horizontalWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textEdit_3 = QtWidgets.QTextEdit(self.horizontalWidget_4)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_4.addWidget(self.textEdit_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_6.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.horizontalWidget_4)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_6.addWidget(self.pushButton_12)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addWidget(self.horizontalWidget_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout_4.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1126, 30))
        self.menubar.setObjectName("menubar")
        self.menuFirst_menu = QtWidgets.QMenu(self.menubar)
        self.menuFirst_menu.setObjectName("menuFirst_menu")
        self.menuSecond_menu = QtWidgets.QMenu(self.menubar)
        self.menuSecond_menu.setObjectName("menuSecond_menu")
        self.menuSubmenu = QtWidgets.QMenu(self.menuSecond_menu)
        self.menuSubmenu.setObjectName("menuSubmenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.style_dw = QtWidgets.QDockWidget(MainWindow)
        self.style_dw.setFloating(False)
        self.style_dw.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.style_dw.setObjectName("style_dw")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setContentsMargins(0, 0, 4, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents_2)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.verticalLayout.addWidget(self.listWidget)
        self.style_dw.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.style_dw)
        self.exit_action = QtWidgets.QAction(MainWindow)
        self.exit_action.setObjectName("exit_action")
        self.actionAction_1 = QtWidgets.QAction(MainWindow)
        self.actionAction_1.setObjectName("actionAction_1")
        self.actionActoin_2 = QtWidgets.QAction(MainWindow)
        self.actionActoin_2.setObjectName("actionActoin_2")
        self.actionAction_3 = QtWidgets.QAction(MainWindow)
        self.actionAction_3.setObjectName("actionAction_3")
        self.menuFirst_menu.addAction(self.exit_action)
        self.menuSubmenu.addAction(self.actionActoin_2)
        self.menuSubmenu.addAction(self.actionAction_3)
        self.menuSecond_menu.addAction(self.actionAction_1)
        self.menuSecond_menu.addAction(self.menuSubmenu.menuAction())
        self.menubar.addAction(self.menuFirst_menu.menuAction())
        self.menubar.addAction(self.menuSecond_menu.menuAction())

        self.retranslateUi(MainWindow)
        self.exit_action.triggered.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.style_trigger_pb.setText(_translate("MainWindow", "Hide style panel"))
        self.table_trigger_pb.setText(_translate("MainWindow", "Hide table"))
        self.text_trigger_pb.setText(_translate("MainWindow", "Hide text panel"))
        self.clear_text_pb.setText(_translate("MainWindow", "Clear text fields"))
        self.add_text_pb.setText(_translate("MainWindow", "Add text field"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Parameter"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Value"))
        self.pushButton.setText(_translate("MainWindow", "Add line"))
        self.pushButton_6.setText(_translate("MainWindow", "Delete line"))
        self.pushButton_9.setText(_translate("MainWindow", "X"))
        self.pushButton_10.setText(_translate("MainWindow", "OK"))
        self.pushButton_11.setText(_translate("MainWindow", "X"))
        self.pushButton_12.setText(_translate("MainWindow", "OK"))
        self.menuFirst_menu.setTitle(_translate("MainWindow", "First menu"))
        self.menuSecond_menu.setTitle(_translate("MainWindow", "Second menu"))
        self.menuSubmenu.setTitle(_translate("MainWindow", "Submenu"))
        self.style_dw.setWindowTitle(_translate("MainWindow", "Style"))
        self.listWidget.setSortingEnabled(False)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "Grey"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "Red"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "Green"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "Blue"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.exit_action.setText(_translate("MainWindow", "Exit"))
        self.exit_action.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAction_1.setText(_translate("MainWindow", "Action 1"))
        self.actionActoin_2.setText(_translate("MainWindow", "Action 2"))
        self.actionAction_3.setText(_translate("MainWindow", "Action 3"))
