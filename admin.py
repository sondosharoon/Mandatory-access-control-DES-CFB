import os
import sys
from PyQt4 import QtCore, QtGui
from add_users import Ui_MainWindow
from disenb import Ui_disenb
from grant import Ui_GiveAdminAccess
from file_create import Ui_CreateFiles
from del_files import Ui_delfiles
from viewfile import Ui_viewfile

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

class Ui_root(object):
    def close_application(self):
        sys.exit();

    def add_users(self):
        self.MainWindow = QtGui.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

    def dis_enb(self):
        self.MainWindow2 = QtGui.QMainWindow()
        self.ui = Ui_disenb()
        self.ui.setupUidis(self.MainWindow2)
        self.MainWindow2.show()

    def grant(self):
        self.GiveAdminAccess = QtGui.QMainWindow()
        self.ui = Ui_GiveAdminAccess()
        self.ui.setupUi(self.GiveAdminAccess)
        self.GiveAdminAccess.show()

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




    def setupUi1(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(368, 399)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../tests/access-control-icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setStyleSheet(_fromUtf8("#Dialog\n"
"{ background-color: qlineargradient(spread:reflect,\n"
"x1:0.5, y1:0, x2:0, y2:0, stop:0 rgba(0, 300, 0, 90),\n"
"stop:1 rgba(32, 80, 96, 100)); }"))
        Dialog.setWindowIcon(icon)
        self.add_user = QtGui.QPushButton(Dialog)
        self.add_user.setGeometry(QtCore.QRect(20, 70, 141, 41))
        self.add_user.setObjectName(_fromUtf8("add_user"))
        self.add_user.clicked.connect(self.add_users)

        self.dis_user = QtGui.QPushButton(Dialog)
        self.dis_user.setGeometry(QtCore.QRect(20, 120, 141, 41))
        self.dis_user.setObjectName(_fromUtf8("dis_user"))
        self.dis_user.clicked.connect(self.dis_enb)


        self.give_admin_access = QtGui.QPushButton(Dialog)
        self.give_admin_access.setGeometry(QtCore.QRect(20, 170, 141, 41))
        self.give_admin_access.setObjectName(_fromUtf8("give_admin_access"))
        self.give_admin_access.clicked.connect(self.grant)

        self.create_files = QtGui.QPushButton(Dialog)
        self.create_files.setGeometry(QtCore.QRect(20, 220, 141, 41))
        self.create_files.setObjectName(_fromUtf8("create_files"))
        self.create_files.clicked.connect(self.write)

        self.del_files = QtGui.QPushButton(Dialog)
        self.del_files.setGeometry(QtCore.QRect(20, 270, 141, 41))
        self.del_files.setObjectName(_fromUtf8("del_files"))
        self.del_files.clicked.connect(self.delete)

        self.view_files = QtGui.QPushButton(Dialog)
        self.view_files.setGeometry(QtCore.QRect(20, 320, 141, 41))
        self.view_files.setObjectName(_fromUtf8("view_files"))
        self.view_files.clicked.connect(self.viewfiles)

        self.exit = QtGui.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(260, 336, 87, 41))
        self.exit.setObjectName(_fromUtf8("exit"))
        self.exit.clicked.connect(self.close_application)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Admin", None))
        self.add_user.setText(_translate("Dialog", "Add User", None))
        self.dis_user.setText(_translate("Dialog", "Disable/Enable User", None))
        self.give_admin_access.setText(_translate("Dialog", "Give admin access", None))
        self.create_files.setText(_translate("Dialog", "Create File", None))
        self.del_files.setText(_translate("Dialog", "Delete FIle", None))
        self.view_files.setText(_translate("Dialog", "View Files", None))
        self.exit.setText(_translate("Dialog", "Exit", None))

