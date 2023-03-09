# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgAboutBdMbFk.ui'
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
        Dialog.resize(267, 231)
        Dialog.setMinimumSize(QSize(267, 231))
        Dialog.setMaximumSize(QSize(267, 231))
        icon = QIcon()
        icon.addFile(u"../imag/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"../imag/icon.png"))

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.commandLinkButton = QCommandLinkButton(Dialog)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(8)
        self.commandLinkButton.setFont(font2)
        self.commandLinkButton.setStyleSheet(u"")
        icon1 = QIcon(QIcon.fromTheme(u"mail"))
        self.commandLinkButton.setIcon(icon1)

        self.verticalLayout.addWidget(self.commandLinkButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Acerca de...", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Youtube List Downloader", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"v2.0.0", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Creado por:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Ranset Fleites", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Dialog", u"ransetfleites0@gmail.com", None))
    # retranslateUi

