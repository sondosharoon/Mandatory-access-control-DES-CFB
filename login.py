#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sqlite3
import sys
import os
import os.path
from user import Ui_Dialog
from admin import Ui_root

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

class Ui_MainWindow(object):
    def signin(self):
        print("printed")
        save_path='database/'
        complete = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(complete)
        cur= db.cursor()
        user = unicode(self.username.text())
        password = unicode(self.password.text())
        f=unicode(cur.execute('SELECT Role FROM users where Username=(?)',(user,)).fetchone()[0])
        g=unicode(cur.execute('SELECT Dis_enb FROM users where Username=(?)',(user,)).fetchone()[0])
        lvl=unicode(cur.execute('SELECT Clearance FROM users where Username=(?)',(user,)).fetchone()[0])
        cur.execute('SELECT * FROM users WHERE Username= ? AND Password = ?', (user,password))
        #f=open("../database/lvl","w")
        #f.write(lvl)
        #f.close()

        if cur.fetchall():
            print(f)
            if(g=='Disable'):
               print("ssss")
            elif(f=='Admin'):
               save_path='database/'
               complete = os.path.join(save_path,"user")
               f=open(complete,"w")
               f.write(user)
               f.close()

               self.Dialog = QtGui.QDialog()
               self.ui = Ui_root()
               self.ui.setupUi1(self.Dialog)
               self.Dialog.show()
            elif (f=='User'):
               save_path='database/'
               complete = os.path.join(save_path,"user")
               f=open(complete,"w")
               f.write(user)
               f.close()

               self.Dialog = QtGui.QDialog()
               self.ui = Ui_Dialog()
               self.ui.setupUi(self.Dialog)
               self.Dialog.show()

        else:
            print("error")

    def cleanup(self):
        self.username.setText("")
        self.password.setText("")

    def close_application(self):
        save_path='database/'
        complete = os.path.join(save_path,"user")
        os.remove(complete)
        sys.exit();


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Login"))
        MainWindow.resize(497, 200)
        MainWindow.setMaximumSize(QtCore.QSize(500, 200))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.login = QtGui.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(270, 140, 87, 27))
        self.login.setObjectName(_fromUtf8("login"))
        ######################################################
        self.login.clicked.connect(self.signin)
        #####################################################

        self.exit = QtGui.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(30, 140, 87, 27))
        self.exit.setObjectName(_fromUtf8("exit"))
        #########################################################
        self.exit.clicked.connect(self.close_application)
        #########################################################


        self.clear = QtGui.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(380, 140, 87, 27))
        self.clear.setObjectName(_fromUtf8("clear"))
        #####################################################
        self.clear.clicked.connect(self.cleanup)
        #####################################################

        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(41, 30, 291, 28))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.username = QtGui.QLineEdit(self.widget)
        self.username.setObjectName(_fromUtf8("username"))
        self.horizontalLayout.addWidget(self.username)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(41, 80, 291, 28))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.password = QtGui.QLineEdit(self.widget1)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.horizontalLayout_2.addWidget(self.password)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Login", "Login", None))
        self.login.setText(_translate("MainWindow", "Login", None))
        self.exit.setText(_translate("MainWindow", "Exit", None))
        self.clear.setText(_translate("MainWindow", "Clear", None))
        self.label.setText(_translate("MainWindow", "Username", None))
        self.label_2.setText(_translate("MainWindow", "Password", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

