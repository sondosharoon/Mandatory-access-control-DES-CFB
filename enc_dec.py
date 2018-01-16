# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from Crypto.Cipher import DES
from Crypto import Random
import base64
import binascii


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

class Ui_encrypt_decrypt(object):
    def padding(self,key,length):
        if(length<8):
            while(length<8):
                key+='A'
                length=len(key)
        elif(length>8):
            while(length>8):
                key = key[:-1]
                length=len(key)
                if(length==8):
                    break
        return key

    def encrypt(self):
        plaintext=unicode(self.lineEdit.text())
        key=unicode(self.lineEdit_2.text())
        iv=unicode(self.lineEdit_3.text())
        length=len(key)
        key_c = self.padding(key,length)
        cipher = DES.new(key_c, DES.MODE_CFB, iv)
        msg=cipher.encrypt(plaintext)
        msg=base64.encodestring(msg)
        self.textEdit.setText(msg)

    def decrypt(self):
        ciphertext=unicode(self.lineEdit.text())
        key=unicode(self.lineEdit_2.text())
        iv=unicode(self.lineEdit_3.text())
        length=len(key)
        key=self.padding(key,length)
        print(key)
        cipher = DES.new(key, DES.MODE_CFB, iv)
        msg=base64.decodestring(ciphertext)
        msg=cipher.decrypt(msg)
        self.textEdit.setText(msg)

    def setupUi(self, encrypt_decrypt):
        encrypt_decrypt.setObjectName(_fromUtf8("encrypt_decrypt"))
        encrypt_decrypt.resize(413, 306)
        encrypt_decrypt.setMaximumSize(QtCore.QSize(413, 307))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../tests/access-control-icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        encrypt_decrypt.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(encrypt_decrypt)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 250, 87, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.encrypt)

        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 250, 87, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(self.decrypt)


        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 371, 31))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.widget1 = QtGui.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 80, 198, 28))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.widget2 = QtGui.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(20, 160, 351, 77))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.widget2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.textEdit = QtGui.QTextEdit(self.widget2)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout_3.addWidget(self.textEdit)
        self.widget3 = QtGui.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(20, 120, 371, 31))
        self.widget3.setObjectName(_fromUtf8("widget3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.widget3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget3)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        encrypt_decrypt.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(encrypt_decrypt)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        encrypt_decrypt.setStatusBar(self.statusbar)

        self.retranslateUi(encrypt_decrypt)
        QtCore.QMetaObject.connectSlotsByName(encrypt_decrypt)

    def retranslateUi(self, encrypt_decrypt):
        encrypt_decrypt.setWindowTitle(_translate("encrypt_decrypt", "Encryptor", None))
        self.pushButton.setText(_translate("encrypt_decrypt", "Encrypt", None))
        self.pushButton_2.setText(_translate("encrypt_decrypt", "Decrypt", None))
        self.label.setText(_translate("encrypt_decrypt", "Enter plaintext/ciphertext", None))
        self.label_3.setText(_translate("encrypt_decrypt", "Enter Key:", None))
        self.label_2.setText(_translate("encrypt_decrypt", "Encrypted", None))
        self.label_4.setText(_translate("encrypt_decrypt", "IV(must be 8 bytes long)", None))
