# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import os
import sqlite3
from pathlib import Path

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

class Ui_CreateFiles(object):
    def save(self):
        TOPSECRET=3
        SECRET=2
        CONFIDENTIAL=1
        UNCLASSIFIED=0

        text=unicode(self.text_2.toPlainText())
        rollybaby = unicode(self.clearance.currentText()) 
        file_name = unicode(self.name.text())
        save_path='database/'
        complete = os.path.join(save_path,"user")
        f=open(complete,"r")
        creator=f.read()
        print(creator+","+rollybaby)
        f.close()
        save_path='database/'
        save = os.path.join(save_path,"user.sqlite")
        db = sqlite3.connect(save)
        cur= db.cursor()
        f=unicode(cur.execute('SELECT creation_auth FROM users where Username=(?)',(creator,)).fetchone()[0])
        admin_or_user=unicode(cur.execute('SELECT Role FROM users where Username=(?)',(creator,)).fetchone()[0])
        cl=unicode(cur.execute('SELECT Clearance FROM users where Username=(?)',(creator,)).fetchone()[0])
        allow=unicode(cur.execute('SELECT creation_auth FROM users where Username=(?)',(creator,)).fetchone()[0])
 
        save_path='database/'
        compp = os.path.join(save_path,file_name)
        my_file = Path(compp)
        if(admin_or_user=="Admin"):
            if my_file.is_file():
                print("exist")
            else: 
                save_path='database/'
                complete = os.path.join(save_path,"user.sqlite")
                db = sqlite3.connect(complete)
                cur= db.cursor()
                cur.execute('Insert into files (File_creator,File_name,Clearance) values(?,?,?)', (creator,file_name,rollybaby))
                db.commit()
                save_path='database/'
                comp = os.path.join(save_path,file_name)
                f=open(comp,"w")
                f.write(text)
                f.close()
        elif(admin_or_user=="User"):
            if my_file.is_file():
                print("exist")
            else:
                if(allow=="Yes"):
                    if(cl=="TOPSECRET"):
                        if(rollybaby=="SECRET"):
                            print("not Allowed") 
                        elif(rollybaby=="CONFIDENTIAL"):
                            print("not Allowed")
                        elif(rollybaby=="UNCLASSIFIED"):
                            print("not Allowed")
                        else:
                            save_path='database/'
                            complete = os.path.join(save_path,"user.sqlite")
                            db = sqlite3.connect(complete)
                            cur= db.cursor()
                            cur.execute('Insert into files (File_creator,File_name,Clearance) values(?,?,?)', (creator,file_name,rollybaby))
                            db.commit()
                            save_path='database/'
                            comp = os.path.join(save_path,file_name)
                            f=open(comp,"w")
                            f.write(text)
                            f.close()
                    elif(cl=="SECRET"):
                        if(rollybaby=="CONFIDENTIAL"):
                            print("not Allowed")
                        elif(rollybaby=="UNCLASSIFIED"):
                            print("not Allowed")
                        else:
                            save_path='database/'
                            complete = os.path.join(save_path,"user.sqlite")
                            db = sqlite3.connect(complete)
                            cur= db.cursor()
                            cur.execute('Insert into files (File_creator,File_name,Clearance) values(?,?,?)', (creator,file_name,rollybaby))
                            db.commit()
                            save_path='database/'
                            comp = os.path.join(save_path,file_name)
                            f=open(comp,"w")
                            f.write(text)
                            f.close()
                    elif(cl=="CONFIDENTIAL"):
                        if(rollybaby=="UNCLASSIFIED"):
                            print("not Allowed")
                        else:
                            save_path='database/'
                            complete = os.path.join(save_path,"user.sqlite")
                            db = sqlite3.connect(complete)
                            cur= db.cursor()
                            cur.execute('Insert into files (File_creator,File_name,Clearance) values(?,?,?)', (creator,file_name,rollybaby))
                            db.commit()
                            save_path='database/'
                            comp = os.path.join(save_path,file_name)
                            f=open(comp,"w")
                            f.write(text)
                            f.close()
                    elif(cl=="UNCLASSIFIED"):
                        if(rollybaby=="UNCLASSIFIED"):
                            save_path='database/'
                            complete = os.path.join(save_path,"user.sqlite")
                            db = sqlite3.connect(complete)
                            cur= db.cursor()
                            cur.execute('Insert into files (File_creator,File_name,Clearance) values(?,?,?)', (creator,file_name,rollybaby))
                            db.commit()
                            save_path='database/'
                            comp = os.path.join(save_path,file_name)
                            f=open(comp,"w")
                            f.write(text)
                            f.close()







    def setupUi(self, CreateFiles):
        CreateFiles.setObjectName(_fromUtf8("CreateFiles"))
        CreateFiles.setEnabled(True)
        CreateFiles.resize(600, 390)
        CreateFiles.setMinimumSize(QtCore.QSize(600, 390))
        CreateFiles.setMaximumSize(QtCore.QSize(600, 390))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../tests/access-control-icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CreateFiles.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(CreateFiles)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 340, 81, 22))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.save)

        self.text_2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.text_2.setGeometry(QtCore.QRect(10, 10, 581, 211))
        self.text_2.setObjectName(_fromUtf8("text_2"))
        self.layoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 290, 214, 28))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget_2)
        self.label_3.setStyleSheet(_fromUtf8("background:white"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.name = QtGui.QLineEdit(self.layoutWidget_2)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout_2.addWidget(self.name)
        self.layoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 250, 211, 31))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(self.layoutWidget_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.clearance = QtGui.QComboBox(self.layoutWidget_4)
        self.clearance.setObjectName(_fromUtf8("clearance"))
        self.clearance.addItem(_fromUtf8(""))
        self.clearance.addItem(_fromUtf8(""))
        self.clearance.addItem(_fromUtf8(""))
        self.clearance.addItem(_fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.clearance)
        CreateFiles.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(CreateFiles)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CreateFiles.setStatusBar(self.statusbar)

        self.retranslateUi(CreateFiles)
        QtCore.QMetaObject.connectSlotsByName(CreateFiles)

    def retranslateUi(self, CreateFiles):
        CreateFiles.setWindowTitle(_translate("CreateFiles", "Create File", None))
        self.pushButton_2.setText(_translate("CreateFiles", "Save", None))
        self.label_3.setText(_translate("CreateFiles", "Enter File name", None))
        self.label_7.setText(_translate("CreateFiles", "Clearance", None))
        self.clearance.setItemText(0, _translate("CreateFiles", "UNCLASSIFIED", None))
        self.clearance.setItemText(1, _translate("CreateFiles", "CONFIDENTIAL", None))
        self.clearance.setItemText(2, _translate("CreateFiles", "SECRET", None))
        self.clearance.setItemText(3, _translate("CreateFiles", "TOPSECRET", None))
