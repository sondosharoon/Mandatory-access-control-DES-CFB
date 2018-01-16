# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import os
import sys
from file_create import Ui_CreateFiles
from del_files import Ui_delfiles
from viewfile import Ui_viewfile
from file_create import Ui_CreateFiles
from enc_dec import Ui_encrypt_decrypt

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

class Ui_Dialog(object):
    def close_application(self):
        save_path='database/'
        complete = os.path.join(save_path,"user")
        os.remove(complete)
        sys.exit();


    def write(self):
        self.CreateFiles = QtGui.QMainWindow()
        self.ui = Ui_CreateFiles()
        self.ui.setupUi(self.CreateFiles)
        self.CreateFiles.show()

    def delete(self):
        self.delfiles = QtGui.QMainWindow()
        self.ui = Ui_delfiles()
        self.ui.setupUidel(self.delfiles)
        self.delfiles.show()

    def viewfiles(self):
        self.viewfile = QtGui.QMainWindow()
        self.ui = Ui_viewfile()
        self.ui.setupUi(self.viewfile)
        self.viewfile.show()

    def crypto(self):
        self.encrypt_decrypt = QtGui.QMainWindow()
        self.ui = Ui_encrypt_decrypt()
        self.ui.setupUi(self.encrypt_decrypt)
        self.encrypt_decrypt.show()



    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(300, 400)
        Dialog.setMaximumSize(QtCore.QSize(300, 400))
        self.encrypt = QtGui.QPushButton(Dialog)
        self.encrypt.setGeometry(QtCore.QRect(80, 290, 111, 41))
        self.encrypt.setObjectName(_fromUtf8("encrypt"))
        self.encrypt.clicked.connect(self.crypto)

        self.write_files = QtGui.QPushButton(Dialog)
        self.write_files.setGeometry(QtCore.QRect(80, 110, 111, 41))
        self.write_files.setObjectName(_fromUtf8("write_files"))
        self.write_files.clicked.connect(self.write)

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.label.setObjectName(_fromUtf8("label"))

        self.view_files = QtGui.QPushButton(Dialog)
        self.view_files.setGeometry(QtCore.QRect(80, 230, 111, 41))
        self.view_files.setObjectName(_fromUtf8("view_files"))
        self.view_files.clicked.connect(self.viewfiles)

        self.delete_files = QtGui.QPushButton(Dialog)
        self.delete_files.setGeometry(QtCore.QRect(80, 170, 111, 41))
        self.delete_files.setObjectName(_fromUtf8("delete_files"))
        self.delete_files.clicked.connect(self.delete)

        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 350, 87, 40))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.close_application)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "User Panel", None))
        self.encrypt.setText(_translate("Dialog", "Encrypt", None))
        self.write_files.setText(_translate("Dialog", "Write Files", None))
        self.label.setText(_translate("Dialog", "TextLabel", None))
        self.view_files.setText(_translate("Dialog", "View files", None))
        self.delete_files.setText(_translate("Dialog", "Delete FIles", None))
        self.pushButton.setText(_translate("Dialog", "Exit", None))

