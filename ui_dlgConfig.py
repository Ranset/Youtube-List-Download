# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgConfigvVuKNO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.ApplicationModal)
        Dialog.resize(362, 104)
        Dialog.setMinimumSize(QSize(362, 104))
        Dialog.setMaximumSize(QSize(362, 104))
        icon = QIcon()
        icon.addFile(u"../imag/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.btnFolder = QPushButton(self.frame)
        self.btnFolder.setObjectName(u"btnFolder")
        self.btnFolder.setMaximumSize(QSize(30, 16777215))
        self.btnFolder.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.btnFolder)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnAceptar = QPushButton(self.frame_2)
        self.btnAceptar.setObjectName(u"btnAceptar")
        self.btnAceptar.setMaximumSize(QSize(86, 16777215))

        self.horizontalLayout_2.addWidget(self.btnAceptar)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configuraci\u00f3n", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Guardar en", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"C:\\", None))
        self.btnFolder.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.btnAceptar.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
    # retranslateUi

