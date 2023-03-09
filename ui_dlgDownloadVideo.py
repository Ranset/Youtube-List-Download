# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlgDownloadVideorKqrdm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_frmDownVideo(object):
    def setupUi(self, frmDownVideo):
        if not frmDownVideo.objectName():
            frmDownVideo.setObjectName(u"frmDownVideo")
        frmDownVideo.resize(523, 203)
        frmDownVideo.setMinimumSize(QSize(523, 203))
        frmDownVideo.setMaximumSize(QSize(523, 203))
        icon = QIcon()
        icon.addFile(u"../imag/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        frmDownVideo.setWindowIcon(icon)
        frmDownVideo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(frmDownVideo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frmTop = QFrame(frmDownVideo)
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

        self.btnGet = QPushButton(self.frmTop)
        self.btnGet.setObjectName(u"btnGet")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGet.sizePolicy().hasHeightForWidth())
        self.btnGet.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"../imag/icons8_download_from_the_cloud_50px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnGet.setIcon(icon1)
        self.btnGet.setIconSize(QSize(32, 32))
        self.btnGet.setAutoDefault(False)
        self.btnGet.setFlat(True)

        self.horizontalLayout.addWidget(self.btnGet)


        self.verticalLayout.addWidget(self.frmTop)

        self.frmCenter = QFrame(frmDownVideo)
        self.frmCenter.setObjectName(u"frmCenter")
        self.frmCenter.setStyleSheet(u"")
        self.frmCenter.setFrameShape(QFrame.StyledPanel)
        self.frmCenter.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frmCenter)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, 0, -1, 0)
        self.label_file = QLabel(self.frmCenter)
        self.label_file.setObjectName(u"label_file")
        self.label_file.setMaximumSize(QSize(50, 16777215))
        self.label_file.setPixmap(QPixmap(u"../imag/icons8_video_file_48px_2.png"))
        self.label_file.setScaledContents(False)

        self.horizontalLayout_3.addWidget(self.label_file)

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
        self.frmDataGrid.setFrameShape(QFrame.StyledPanel)
        self.frmDataGrid.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frmDataGrid)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setContentsMargins(0, 0, -1, -1)
        self.label_2 = QLabel(self.frmDataGrid)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(115, 115, 115);")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_5 = QLabel(self.frmDataGrid)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_5)

        self.label_3 = QLabel(self.frmDataGrid)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(115, 115, 115);")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_6 = QLabel(self.frmDataGrid)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_6)

        self.label_7 = QLabel(self.frmDataGrid)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_7)

        self.label_4 = QLabel(self.frmDataGrid)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(115, 115, 115);")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)


        self.verticalLayout_2.addWidget(self.frmDataGrid)


        self.horizontalLayout_3.addWidget(self.frmDatos)


        self.verticalLayout.addWidget(self.frmCenter)

        self.frmBottom = QFrame(frmDownVideo)
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

        self.btnAgregar = QPushButton(self.frmBottom)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setEnabled(False)
        font3 = QFont()
        font3.setBold(True)
        font3.setWeight(75)
        self.btnAgregar.setFont(font3)

        self.horizontalLayout_2.addWidget(self.btnAgregar)

        self.btnCancel = QPushButton(self.frmBottom)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setFont(font3)

        self.horizontalLayout_2.addWidget(self.btnCancel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frmBottom)


        self.retranslateUi(frmDownVideo)

        QMetaObject.connectSlotsByName(frmDownVideo)
    # setupUi

    def retranslateUi(self, frmDownVideo):
        frmDownVideo.setWindowTitle(QCoreApplication.translate("frmDownVideo", u"Bajar video", None))
        self.label.setText(QCoreApplication.translate("frmDownVideo", u"URL:", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("frmDownVideo", u"Coloque la direcci\u00f3n del video", None))
#if QT_CONFIG(whatsthis)
        self.btnGet.setWhatsThis(QCoreApplication.translate("frmDownVideo", u"Presione para comenzar a buscar el video a descargar.", None))
#endif // QT_CONFIG(whatsthis)
        self.lblVideoName.setText(QCoreApplication.translate("frmDownVideo", u"Nombre del video", None))
        self.label_2.setText(QCoreApplication.translate("frmDownVideo", u"Duraci\u00f3n:", None))
        self.label_5.setText(QCoreApplication.translate("frmDownVideo", u"00:00:00", None))
        self.label_3.setText(QCoreApplication.translate("frmDownVideo", u"Tama\u00f1o:", None))
        self.label_6.setText(QCoreApplication.translate("frmDownVideo", u"33MB", None))
        self.label_7.setText(QCoreApplication.translate("frmDownVideo", u"c:/Download", None))
        self.label_4.setText(QCoreApplication.translate("frmDownVideo", u"Path:", None))
        self.btnAgregar.setText(QCoreApplication.translate("frmDownVideo", u"Agregar", None))
        self.btnCancel.setText(QCoreApplication.translate("frmDownVideo", u"Cancelar", None))
    # retranslateUi

