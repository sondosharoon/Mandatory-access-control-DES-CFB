# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sqlite3
import os
import sys
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

class Ui_disenb(object):
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

#############For disabling users only i hope they wont cry like 5 yea ! #################

    def disable1(self):
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)
        cur= db.cursor()
        disable = unicode(self.disable.text())
        cur.execute('Update users set Dis_enb="Disable" where Username=(?)',(disable,))
        db.commit()

    def enable(self):
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)

        cur= db.cursor()
        enable = unicode(self.disable.text())
        cur.execute('Update users set Dis_enb="Enable" where Username=(?)',(enable,))
        db.commit()
############################################################################################
#########################stop them from deleting the only way they shall not passssssss the mordorr################

    def dis_del(self):
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)

        cur= db.cursor()
        disable = unicode(self.delete_2.text())
        cur.execute('Update users set deletion_auth="No" where Username=(?)',(disable,))
        db.commit()

    def enb_del(self):
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)

        cur= db.cursor()
        enable = unicode(self.delete_2.text())
        cur.execute('Update users set deletion_auth="Yes" where Username=(?)',(enable,))
        db.commit()
###################################################################################################################
#########################The histroy shall be created by only the one who remains in power#########################
    def dis_create(self):
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)

        cur= db.cursor()
        disable = unicode(self.create.text())
        cur.execute('Update users set creation_auth="No" where Username=(?)',(disable,))
        db.commit()

    def enb_create(self):
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)

        cur= db.cursor()
        enable = unicode(self.create.text())
        cur.execute('Update users set creation_auth="Yes" where Username=(?)',(enable,))
        db.commit()
####################################################################################################################
########################################You shall not seee through the walls of the china##########################
    def dis_access(self):
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)

        cur= db.cursor()
        disable = unicode(self.access.text())
        cur.execute('Update users set access_auth="No" where Username=(?)',(disable,))
        db.commit()

    def enb_access(self):
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)

        cur= db.cursor()
        enable = unicode(self.access.text())
        cur.execute('Update users set access_auth="Yes" where Username=(?)',(enable,))
        db.commit()
####################################################################################################################

    def setupUidis(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(432, 443)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../tests/access-control-icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Load = QtGui.QPushButton(self.centralwidget)
        self.Load.setGeometry(QtCore.QRect(10, 60, 87, 27))
        self.Load.setObjectName(_fromUtf8("Load"))
        self.Load.clicked.connect(self.loading)


        self.grant_disable = QtGui.QPushButton(self.centralwidget)
        self.grant_disable.setGeometry(QtCore.QRect(80, 150, 87, 27))
        self.grant_disable.setObjectName(_fromUtf8("grant_disable"))
        self.grant_disable.clicked.connect(self.enable)

        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 120, 391, 31))
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
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 190, 391, 31))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.delete_2 = QtGui.QLineEdit(self.layoutWidget_2)
        self.delete_2.setText(_fromUtf8(""))
        self.delete_2.setObjectName(_fromUtf8("delete_2"))

        self.horizontalLayout_2.addWidget(self.delete_2)
        self.grant_delete = QtGui.QPushButton(self.centralwidget)
        self.grant_delete.setGeometry(QtCore.QRect(90, 220, 87, 27))
        self.grant_delete.setObjectName(_fromUtf8("grant_delete"))
        self.grant_delete.clicked.connect(self.enb_del)

        self.layoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 260, 391, 31))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.create = QtGui.QLineEdit(self.layoutWidget_3)
        self.create.setObjectName(_fromUtf8("create"))
        self.horizontalLayout_3.addWidget(self.create)
        self.grant_create = QtGui.QPushButton(self.centralwidget)
        self.grant_create.setGeometry(QtCore.QRect(100, 300, 87, 27))
        self.grant_create.setObjectName(_fromUtf8("grant_create"))
        self.grant_create.clicked.connect(self.enb_create)
     
        self.grant_create2 = QtGui.QPushButton(self.centralwidget)
        self.grant_create2.setGeometry(QtCore.QRect(200, 300, 87, 27))
        self.grant_create2.setObjectName(_fromUtf8("grant_create2"))
        self.grant_create2.clicked.connect(self.dis_create)

        self.grant_disable2 = QtGui.QPushButton(self.centralwidget)
        self.grant_disable2.setGeometry(QtCore.QRect(170, 150, 87, 27))
        self.grant_disable2.setObjectName(_fromUtf8("grant_disable2"))
        self.grant_disable2.clicked.connect(self.disable1)

        self.grant_delete2 = QtGui.QPushButton(self.centralwidget)
        self.grant_delete2.setGeometry(QtCore.QRect(180, 220, 87, 27))
        self.grant_delete2.setObjectName(_fromUtf8("grant_delete2"))
        self.grant_delete2.clicked.connect(self.dis_del)

        self.grant_access2 = QtGui.QPushButton(self.centralwidget)
        self.grant_access2.setGeometry(QtCore.QRect(200, 380, 87, 27))
        self.grant_access2.setObjectName(_fromUtf8("grant_access2"))
        self.grant_access2.clicked.connect(self.dis_access)

        self.layoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 340, 391, 31))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.layoutWidget_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.access = QtGui.QLineEdit(self.layoutWidget_4)
        self.access.setObjectName(_fromUtf8("access"))
        self.horizontalLayout_4.addWidget(self.access)
        self.grant_Access = QtGui.QPushButton(self.centralwidget)
        self.grant_Access.setGeometry(QtCore.QRect(100, 380, 87, 27))
        self.grant_Access.setObjectName(_fromUtf8("grant_Access"))
        self.grant_Access.clicked.connect(self.enb_access)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Disable/Enable User", None))
        self.Load.setText(_translate("MainWindow", "Load users", None))
        self.grant_disable.setText(_translate("MainWindow", "Grant", None))
        self.label.setText(_translate("MainWindow", "Enter Username to disable:", None))
        self.label_2.setText(_translate("MainWindow", "Enter Username to Allow/Deny Deleting:", None))
        self.grant_delete.setText(_translate("MainWindow", "Grant", None))
        self.label_3.setText(_translate("MainWindow", "Enter Username to Allow/Deny Create File:", None))
        self.grant_create.setText(_translate("MainWindow", "Grant", None))
        self.grant_create2.setText(_translate("MainWindow", "Deny", None))
        self.grant_disable2.setText(_translate("MainWindow", "Deny", None))
        self.grant_delete2.setText(_translate("MainWindow", "Deny", None))
        self.grant_access2.setText(_translate("MainWindow", "Deny", None))
        self.label_4.setText(_translate("MainWindow", "Enter Username to Allow/Deny Access:", None))
        self.grant_Access.setText(_translate("MainWindow", "Grant", None))
