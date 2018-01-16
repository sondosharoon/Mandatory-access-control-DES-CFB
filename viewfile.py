# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import os
import sqlite3
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

class Ui_viewfile(object):
    def loading(self):
        save_path='database/'
        complete = os.path.join(save_path,"user")
        f=open(complete,"r")
        creator=f.read()
        f.close()
        ############so finally i came up with something###########
        #TOPSECRET=4
        #SECRET=3
        #CONFIDENTIAL=2
        #UNCLASSIFIED=1
        ############never under estimate your opponent###############

        print(creator)
        save_path='database/'
        comp = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(comp)
        cur= db.cursor()
        f=unicode(cur.execute('SELECT Role FROM users where Username=(?)',(creator,)).fetchone()[0])
        cl=unicode(cur.execute('SELECT Clearance  FROM users where Username=(?)',(creator,)).fetchone()[0])
        allow=unicode(cur.execute('SELECT access_auth FROM users where Username=(?)',(creator,)).fetchone()[0])
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
            if(allow=="Yes"):
                if(cl =="TOPSECRET"):
                    save_path='database/'
                    save = os.path.join(save_path,"user.sqlite")
                    db = sqlite3.connect(save)
                    cur= db.cursor()

                    complete = os.path.join(save_path,"user.sqlite")
                    db = QSqlDatabase.addDatabase("QSQLITE")
                    db.setDatabaseName(complete)
                    db.open()
                    View = QSqlQueryModel()
                    View.setQuery("SELECT * FROM files where Clearance in('TOPSECRET','SECRET','CONFIDENTIAL','UNCLASSIFIED')",db)
                    self.tableView = QtGui.QTableView()
                    self.tableView.setModel(View)
                    self.tableView.show()
                elif(cl =="SECRET"):
                    save_path='database/'
                    save = os.path.join(save_path,"user.sqlite")
                    db = sqlite3.connect(save)
                    cur= db.cursor()

                    complete = os.path.join(save_path,"user.sqlite")
                    db = QSqlDatabase.addDatabase("QSQLITE")
                    db.setDatabaseName(complete)
                    db.open()
                    View = QSqlQueryModel()
                    View.setQuery("SELECT * FROM files where Clearance in('SECRET','CONFIDENTIAL','UNCLASSIFIED')",db)
                    self.tableView = QtGui.QTableView()
                    self.tableView.setModel(View)
                    self.tableView.show()
                elif(cl =="CONFIDENTIAL"):
                    save_path='database/'
                    save = os.path.join(save_path,"user.sqlite")
                    db = sqlite3.connect(save)
                    cur= db.cursor()

                    complete = os.path.join(save_path,"user.sqlite")
                    db = QSqlDatabase.addDatabase("QSQLITE")
                    db.setDatabaseName(complete)
                    db.open()
                    View = QSqlQueryModel()
                    View.setQuery("SELECT * FROM files where Clearance in('CONFIDENTIAL','UNCLASSIFIED')",db)
                    self.tableView = QtGui.QTableView()
                    self.tableView.setModel(View)
                    self.tableView.show()
                elif(cl =="UNCLASSIFIED"):
                    save_path='database/'
                    save = os.path.join(save_path,"user.sqlite")
                    db = sqlite3.connect(save)
                    cur= db.cursor()

                    complete = os.path.join(save_path,"user.sqlite")
                    db = QSqlDatabase.addDatabase("QSQLITE")
                    db.setDatabaseName(complete)
                    db.open()
                    View = QSqlQueryModel()
                    View.setQuery("SELECT * FROM files where Clearance in('UNCLASSIFIED')",db)
                    self.tableView = QtGui.QTableView()
                    self.tableView.setModel(View)
                    self.tableView.show()



    def reading(self):
        ###########sometime i love to read my own body languge ##################
        save_path='database/'
        complete = os.path.join(save_path,"user")
        f=open(complete,"r")
        creator=f.read()
        f.close()
        ##########and record it as a memory in some of my flipflops##############


        ############sometime you can't escape the reality############
        TOPSECRET=5
        SECRET=4
        CONFIDENTIAL=3
        UNCLASSIFIED=2
        ############never under estimate your opponent###############

        rd=unicode(self.read.text())
        #######Pulling out file info##############
        save_path='database/'
        comp = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(comp)
        cur= db.cursor()
        f=unicode(cur.execute('SELECT Clearance FROM files where File_name=(?)',(rd,)).fetchone()[0])
        ad=unicode(cur.execute('SELECT Role FROM users where Username=(?)',(creator,)).fetchone()[0])  #This is for admin or user
        lvl=unicode(cur.execute('SELECT Clearance FROM users where Username=(?)',(creator,)).fetchone()[0])
        allow=unicode(cur.execute('SELECT access_auth FROM users where Username=(?)',(creator,)).fetchone()[0])
        db.close()
        if(ad=="Admin"):
            save_path='database/'
            complete = os.path.join(save_path,rd)
            f=open(complete,"r")
            creator=f.read()
            f.close()
            self.textEdit.setText(creator)
        elif(ad=="User"):
            if(allow=="Yes"):
        ############sometime you can't escape the reality############
                TOPSECRET=4
                SECRET=3
                CONFIDENTIAL=2
                UNCLASSIFIED=1
        ############never under estimate your opponent###############
                if(lvl=="TOPSECRET"):
                    save_path='database/'
                    complete = os.path.join(save_path,rd)
                    f=open(complete,"r")
                    creator=f.read()
                    f.close()
                    self.textEdit.setText(creator)
                elif(lvl=="SECRET"):
                    if(f=="TOPSECRET"):
                        print("Not allowed")
                    else:
                        save_path='database/'
                        complete = os.path.join(save_path,rd)
                        f=open(complete,"r")
                        creator=f.read()
                        f.close()
                        self.textEdit.setText(creator)

                elif(lvl=="CONFIDENTIAL"):
                    if(f=="TOPSECRET"):
                        print("not allowed")
                    elif(f=="SECRET"):
                        print("not allowed")
                    else:
                        save_path='database/'
                        complete = os.path.join(save_path,rd)
                        f=open(complete,"r")
                        creator=f.read()
                        f.close()
                        self.textEdit.setText(creator)
                elif(lvl=="UNCLASSIFIED"):
                    if(f=="TOPSECRET"):
                        print("not allowed")
                    elif(f=="SECRET"):
                        print("not allowed")
                    elif(f=="CONFIDENTIAL"):
                        print("not allowed")
                    else:
                        save_path='database/'
                        complete = os.path.join(save_path,rd)
                        f=open(complete,"r")
                        creator=f.read()
                        f.close()
                        self.textEdit.setText(creator)
  




    def setupUi(self, viewfile):
        viewfile.setObjectName(_fromUtf8("viewfile"))
        viewfile.resize(682, 355)
        viewfile.setMaximumSize(QtCore.QSize(682, 355))
        self.centralwidget = QtGui.QWidget(viewfile)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 371, 231))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(730, 620, 81, 22))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.reader = QtGui.QPushButton(self.centralwidget)
        self.reader.setGeometry(QtCore.QRect(310, 300, 87, 27))
        self.reader.setObjectName(_fromUtf8("reader"))
        self.reader.clicked.connect(self.reading)
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 260, 331, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.read = QtGui.QLineEdit(self.layoutWidget)
        self.read.setObjectName(_fromUtf8("read"))
        self.horizontalLayout.addWidget(self.read)
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(420, 10, 256, 231))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(460, 250, 183, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.load = QtGui.QPushButton(self.widget)
        self.load.setObjectName(_fromUtf8("load"))
        self.load.clicked.connect(self.loading)

        self.horizontalLayout_2.addWidget(self.load)
        viewfile.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(viewfile)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        viewfile.setStatusBar(self.statusbar)

        self.retranslateUi(viewfile)
        QtCore.QMetaObject.connectSlotsByName(viewfile)

    def retranslateUi(self, viewfile):
        viewfile.setWindowTitle(_translate("viewfile", "MainWindow", None))
        self.pushButton_3.setText(_translate("viewfile", "OK", None))
        self.reader.setText(_translate("viewfile", "Read", None))
        self.label.setText(_translate("viewfile", "Enter file name:", None))
        self.label_2.setText(_translate("viewfile", "View file name", None))
        self.load.setText(_translate("viewfile", "Load", None))
