# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgDownloadListKCmvDM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_frmDownList(object):
    def setupUi(self, frmDownList):
        if not frmDownList.objectName():
            frmDownList.setObjectName(u"frmDownList")
        frmDownList.resize(600, 263)
        frmDownList.setMinimumSize(QSize(600, 263))
        frmDownList.setMaximumSize(QSize(600, 263))
        icon = QIcon()
        icon.addFile(u"../imag/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        frmDownList.setWindowIcon(icon)
        frmDownList.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        frmDownList.setModal(True)
        self.verticalLayout = QVBoxLayout(frmDownList)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frmTop = QFrame(frmDownList)
        self.frmTop.setObjectName(u"frmTop")
        self.frmTop.setMaximumSize(QSize(16777215, 51))
        self.frmTop.setStyleSheet(u"QFrame{\n"
"background-color: rgb(51, 58, 77);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 2px;\n"
"}")
        self.frmTop.setFrameShape(QFrame.StyledPanel)
        self.frmTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frmTop)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frmTop)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.RichText)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frmTop)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 23))
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit.setFont(font1)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frmTop)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"../imag/icons8_download_from_the_cloud_50px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(32, 32))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frmTop)

        self.frmCenter = QFrame(frmDownList)
        self.frmCenter.setObjectName(u"frmCenter")
        self.frmCenter.setStyleSheet(u"")
        self.frmCenter.setFrameShape(QFrame.StyledPanel)
        self.frmCenter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frmCenter)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(100, 0, -1, 0)
        self.frmDatos = QFrame(self.frmCenter)
        self.frmDatos.setObjectName(u"frmDatos")
        self.frmDatos.setFrameShape(QFrame.StyledPanel)
        self.frmDatos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frmDatos)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lblVideoName = QLabel(self.frmDatos)
        self.lblVideoName.setObjectName(u"lblVideoName")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setWeight(75)
        self.lblVideoName.setFont(font2)

        self.verticalLayout_2.addWidget(self.lblVideoName)

        self.frmDataGrid = QFrame(self.frmDatos)
        self.frmDataGrid.setObjectName(u"frmDataGrid")
        self.frmDataGrid.setStyleSheet(u"QProgressBar {\n"
"	text-align: center;\n"
"	background-color: lightgrey;\n"
"	border-radius: 4px;\n"
"	max-height: 8px;\n"
"	max-width: 280px;\n"
"	margin-top: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: #16A4F8;\n"
"	border-radius: 4px;\n"
"	\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 10pt;\n"
"}")
        self.frmDataGrid.setFrameShape(QFrame.StyledPanel)
        self.frmDataGrid.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frmDataGrid)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, -1, -1, -1)
        self.label_8 = QLabel(self.frmDataGrid)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: rgb(115, 115, 115);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.progressBar = QProgressBar(self.frmDataGrid)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.progressBar)

        self.label_11 = QLabel(self.frmDataGrid)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(115, 115, 115);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.label_9 = QLabel(self.frmDataGrid)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_9)

        self.label_10 = QLabel(self.frmDataGrid)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(115, 115, 115);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_10)

        self.label_12 = QLabel(self.frmDataGrid)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_12)

        self.label_2 = QLabel(self.frmDataGrid)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(115, 115, 115);")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.label_5 = QLabel(self.frmDataGrid)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_5)

        self.label_3 = QLabel(self.frmDataGrid)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(115, 115, 115);")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_3)

        self.label_6 = QLabel(self.frmDataGrid)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_6)

        self.label_4 = QLabel(self.frmDataGrid)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(115, 115, 115);")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.label_7 = QLabel(self.frmDataGrid)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_7)


        self.verticalLayout_2.addWidget(self.frmDataGrid)


        self.horizontalLayout_3.addWidget(self.frmDatos)


        self.verticalLayout.addWidget(self.frmCenter)

        self.frmBottom = QFrame(frmDownList)
        self.frmBottom.setObjectName(u"frmBottom")
        self.frmBottom.setMaximumSize(QSize(16777215, 44))
        self.frmBottom.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(51, 58, 77);\n"
"color: white;\n"
"border-radius: 4px;\n"
"border: 5px solid  rgb(51, 58, 77);\n"
"padding: 2px 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(89, 102, 135);\n"
"	border: 5px solid  rgb(89, 102, 135);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border: 5px solid  rgb(206, 206, 206);\n"
"}")
        self.frmBottom.setFrameShape(QFrame.StyledPanel)
        self.frmBottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frmBottom)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.frmBottom)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.frmBottom)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setFont(font3)

        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frmBottom)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font3)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frmBottom)


        self.retranslateUi(frmDownList)

        QMetaObject.connectSlotsByName(frmDownList)
    # setupUi

    def retranslateUi(self, frmDownList):
        frmDownList.setWindowTitle(QCoreApplication.translate("frmDownList", u"Bajar Lista", None))
        self.label.setText(QCoreApplication.translate("frmDownList", u"URL:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("frmDownList", u"Coloque la direcci\u00f3n de la lista", None))
#if QT_CONFIG(whatsthis)
        self.pushButton.setWhatsThis(QCoreApplication.translate("frmDownList", u"Presione para comenzar a buscar los videos a descargar.", None))
#endif // QT_CONFIG(whatsthis)
        self.lblVideoName.setText(QCoreApplication.translate("frmDownList", u"Obteniendo lista: \"Nombre de la lista\"", None))
        self.label_8.setText(QCoreApplication.translate("frmDownList", u"Completado", None))
        self.label_11.setText(QCoreApplication.translate("frmDownList", u"T\u00edtulo:", None))
        self.label_9.setText(QCoreApplication.translate("frmDownList", u"T\u00edtulo del video", None))
        self.label_10.setText(QCoreApplication.translate("frmDownList", u"Video:", None))
        self.label_12.setText(QCoreApplication.translate("frmDownList", u"1 de 28", None))
        self.label_2.setText(QCoreApplication.translate("frmDownList", u"Duraci\u00f3n:", None))
        self.label_5.setText(QCoreApplication.translate("frmDownList", u"00:00:00", None))
        self.label_3.setText(QCoreApplication.translate("frmDownList", u"Tama\u00f1o:", None))
        self.label_6.setText(QCoreApplication.translate("frmDownList", u"15MB", None))
        self.label_4.setText(QCoreApplication.translate("frmDownList", u"Path:", None))
        self.label_7.setText(QCoreApplication.translate("frmDownList", u"c:/Download", None))
        self.pushButton_2.setText(QCoreApplication.translate("frmDownList", u"Agregar", None))
        self.pushButton_4.setText(QCoreApplication.translate("frmDownList", u"Ver txt", None))
        self.pushButton_3.setText(QCoreApplication.translate("frmDownList", u"Cancelar", None))
    # retranslateUi

