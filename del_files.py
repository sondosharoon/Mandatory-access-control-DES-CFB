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

class Ui_delfiles(object):
    def loading(self):
        save_path='database/'
        complete = os.path.join(save_path,"user")
        f=open(complete,"r")
        creator=f.read()
        f.close()

        print(creator)
        save_path='database/'
        comp = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(comp)
        cur= db.cursor()
        f=unicode(cur.execute('SELECT Role FROM users where Username=(?)',(creator,)).fetchone()[0])
        db.close()

        if(f=="Admin"):
            save_path='database/'
            complete = os.path.join(save_path,"user.sqlite")
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(complete)
            db.open()
            View = QSqlQueryModel()
            View.setQuery("select * from Files",db)
            self.tableView = QtGui.QTableView()
            self.tableView.setModel(View)
            self.tableView.show()
        elif(f=='User'):
            save_path='database/'
            save = os.path.join(save_path,"user.sqlite")
            db = sqlite3.connect(save)
            cur= db.cursor()
            f = """SELECT * FROM Files where File_creator=('%s')"""%(creator)   #This shit cost me a lot i will never forget

            complete = os.path.join(save_path,"user.sqlite")
            db = QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(complete)
            db.open()
            View = QSqlQueryModel()
            View.setQuery(f,db)
            self.tableView = QtGui.QTableView()
            self.tableView.setModel(View)
            self.tableView.show()


    def delete(self):
        delete=unicode(self.delete.text())
        save_path='database/'
        complete = os.path.join(save_path,"user")
        f=open(complete,"r")
        creator=f.read()
        f.close()

        save_path='database/'
        save = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(save)
        cur= db.cursor()
        f=unicode(cur.execute('SELECT deletion_auth FROM users where Username=(?)',(creator,)).fetchone()[0])
        owner=unicode(cur.execute('SELECT File_creator FROM files where File_name=(?)',(delete,)).fetchone()[0])
        admin_or_user=unicode(cur.execute('SELECT Role FROM users where Username=(?)',(creator,)).fetchone()[0])
        if(admin_or_user=="Admin"):
            print("gone")   
            save_path='database/'
            complete = os.path.join(save_path,delete)
            os.remove(complete)
            cur.execute("delete from files where File_name=(?)",(delete,))
            db.commit()


        else:
            if (f=="Yes"):
                if(owner==creator):
                    save_path='database/'
                    complete = os.path.join(save_path,delete)
                    os.remove(complete)
                    cur.execute("delete from files where File_name=(?)",(delete,))
                    db.commit()

        print("done")


        
    def setupUidel(self, delfiles):
        delfiles.setObjectName(_fromUtf8("delfiles"))
        delfiles.resize(442, 375)
        delfiles.setMinimumSize(QtCore.QSize(442, 375))
        delfiles.setMaximumSize(QtCore.QSize(442, 375))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../tests/access-control-icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        delfiles.setWindowIcon(icon)
        delfiles.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(delfiles)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 290, 81, 22))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.delete)


        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 431, 231))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 87, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.loading)

        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 290, 232, 28))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.delete = QtGui.QLineEdit(self.widget)
        self.delete.setObjectName(_fromUtf8("delete"))

        self.horizontalLayout.addWidget(self.delete)
        delfiles.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(delfiles)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        delfiles.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(delfiles)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        delfiles.setStatusBar(self.statusbar)

        self.retranslateUi(delfiles)
        QtCore.QMetaObject.connectSlotsByName(delfiles)

    def retranslateUi(self, delfiles):
        delfiles.setWindowTitle(_translate("delfiles", "Delete Files", None))
        self.pushButton_3.setText(_translate("delfiles", "Delete", None))
        self.pushButton.setText(_translate("delfiles", "Load Files", None))
        self.label_2.setText(_translate("delfiles", "Enter File name", None))


