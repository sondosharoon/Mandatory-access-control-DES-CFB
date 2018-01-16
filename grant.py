# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui
import sqlite3
import os
from PyQt4.QtSql import QSqlQueryModel,QSqlDatabase,QSqlQuery

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GiveAdminAccess(object):
    def loading(self):
        db = QSqlDatabase.addDatabase("QSQLITE")
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db.setDatabaseName(complete)
        db.open()

        View = QSqlQueryModel()
        View.setQuery("select * from users",db)
        self.tableView = QtGui.QTableView()
        self.tableView.setModel(View)
        self.tableView.show()


    def user(self):
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)
        cur= db.cursor()
        disable = unicode(self.disable_2.text())
        cur.execute('update users set Role="User" where Username=(?)',(disable,))
        db.commit()

    def admin(self):
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)
        cur= db.cursor()
        enable = unicode(self.disable.text())
        cur.execute('update users set Role="Admin" where Username=(?)',(enable,))
        db.commit()

    def setupUi(self, GiveAdminAccess):
        GiveAdminAccess.setObjectName(_fromUtf8("GiveAdminAccess"))
        GiveAdminAccess.resize(576, 403)
        self.centralwidget = QtGui.QWidget(GiveAdminAccess)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Load = QtGui.QPushButton(self.centralwidget)
        self.Load.setGeometry(QtCore.QRect(30, 260, 87, 27))
        self.Load.setObjectName(_fromUtf8("Load"))
        self.Load.clicked.connect(self.loading)

        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 290, 401, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.disable = QtGui.QLineEdit(self.layoutWidget)
        self.disable.setObjectName(_fromUtf8("disable"))
        self.horizontalLayout.addWidget(self.disable)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(30, 20, 271, 231))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.grant = QtGui.QPushButton(self.centralwidget)
        self.grant.setGeometry(QtCore.QRect(440, 290, 87, 27))
        self.grant.setObjectName(_fromUtf8("grant"))
        self.grant.clicked.connect(self.admin)

        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 330, 401, 31))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.disable_2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.disable_2.setObjectName(_fromUtf8("disable_2"))
        self.horizontalLayout_2.addWidget(self.disable_2)
        self.user_access = QtGui.QPushButton(self.centralwidget)
        self.user_access.setGeometry(QtCore.QRect(440, 330, 87, 27))
        self.user_access.setObjectName(_fromUtf8("user_access"))
        self.user_access.clicked.connect(self.user)

        GiveAdminAccess.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(GiveAdminAccess)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        GiveAdminAccess.setStatusBar(self.statusbar)

        self.retranslateUi(GiveAdminAccess)
        QtCore.QMetaObject.connectSlotsByName(GiveAdminAccess)

    def retranslateUi(self, GiveAdminAccess):
        GiveAdminAccess.setWindowTitle(_translate("GiveAdminAccess", "Give Admin Access", None))
        self.Load.setText(_translate("GiveAdminAccess", "Load users", None))
        self.label.setText(_translate("GiveAdminAccess", "Enter Username to give admin access:", None))
        self.grant.setText(_translate("GiveAdminAccess", "Grant", None))
        self.label_2.setText(_translate("GiveAdminAccess", "Enter Username to give User access:", None))
        self.user_access.setText(_translate("GiveAdminAccess", "Grant", None))

