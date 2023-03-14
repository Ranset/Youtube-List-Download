# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainAWLUtj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QSize(640, 480))
        icon = QIcon()
        icon.addFile(u"../imag/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.frmBotones = QFrame(self.centralwidget)
        self.frmBotones.setObjectName(u"frmBotones")
        self.frmBotones.setMaximumSize(QSize(16777215, 51))
        self.frmBotones.setAutoFillBackground(False)
        self.frmBotones.setStyleSheet(u"background-color: rgb(51, 58, 77);")
        self.frmBotones.setFrameShape(QFrame.StyledPanel)
        self.frmBotones.setFrameShadow(QFrame.Raised)
        self.frmBotones.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.frmBotones)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnVideo = QPushButton(self.frmBotones)
        self.btnVideo.setObjectName(u"btnVideo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(64)
        sizePolicy.setVerticalStretch(64)
        sizePolicy.setHeightForWidth(self.btnVideo.sizePolicy().hasHeightForWidth())
        self.btnVideo.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"../imag/icons8_video_file_30px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnVideo.setIcon(icon1)
        self.btnVideo.setIconSize(QSize(30, 30))
        self.btnVideo.setFlat(True)

        self.horizontalLayout.addWidget(self.btnVideo)

        self.btnLista = QPushButton(self.frmBotones)
        self.btnLista.setObjectName(u"btnLista")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnLista.sizePolicy().hasHeightForWidth())
        self.btnLista.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u"../imag/icons8_video_playlist_30px_3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLista.setIcon(icon2)
        self.btnLista.setIconSize(QSize(30, 30))
        self.btnLista.setFlat(True)

        self.horizontalLayout.addWidget(self.btnLista)

        self.btnTrash = QPushButton(self.frmBotones)
        self.btnTrash.setObjectName(u"btnTrash")
        sizePolicy1.setHeightForWidth(self.btnTrash.sizePolicy().hasHeightForWidth())
        self.btnTrash.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u"../imag/icons8_trash_24px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnTrash.setIcon(icon3)
        self.btnTrash.setIconSize(QSize(30, 30))
        self.btnTrash.setFlat(True)

        self.horizontalLayout.addWidget(self.btnTrash)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnConfig = QPushButton(self.frmBotones)
        self.btnConfig.setObjectName(u"btnConfig")
        sizePolicy1.setHeightForWidth(self.btnConfig.sizePolicy().hasHeightForWidth())
        self.btnConfig.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u"../imag/icons8_settings_24px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnConfig.setIcon(icon4)
        self.btnConfig.setIconSize(QSize(30, 30))
        self.btnConfig.setFlat(True)

        self.horizontalLayout.addWidget(self.btnConfig)


        self.verticalLayout.addWidget(self.frmBotones)

        self.frmGrid = QFrame(self.centralwidget)
        self.frmGrid.setObjectName(u"frmGrid")
        self.frmGrid.setFrameShape(QFrame.StyledPanel)
        self.frmGrid.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frmGrid)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.table = QTableWidget(self.frmGrid)
        if (self.table.columnCount() < 5):
            self.table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.table.setObjectName(u"table")
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.table)


        self.verticalLayout.addWidget(self.frmGrid)

        self.frmControls = QFrame(self.centralwidget)
        self.frmControls.setObjectName(u"frmControls")
        self.frmControls.setMaximumSize(QSize(16777215, 62))
        self.frmControls.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(51, 58, 77);\n"
"color: rgb(161, 173, 199);\n"
"border-radius: 6px;\n"
"border: 5px solid  rgb(51, 58, 77);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"	background-color: rgb(206, 206, 206);\n"
"	border: 5px solid  rgb(206, 206, 206);\n"
"}")
        self.frmControls.setFrameShape(QFrame.StyledPanel)
        self.frmControls.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frmControls)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnStart = QPushButton(self.frmControls)
        self.btnStart.setObjectName(u"btnStart")
        sizePolicy1.setHeightForWidth(self.btnStart.sizePolicy().hasHeightForWidth())
        self.btnStart.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamily(u"Corbel")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.btnStart.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u"../imag/icons8_download_26px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnStart.setIcon(icon5)
        self.btnStart.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btnStart)

        self.btnPause = QPushButton(self.frmControls)
        self.btnPause.setObjectName(u"btnPause")
        sizePolicy1.setHeightForWidth(self.btnPause.sizePolicy().hasHeightForWidth())
        self.btnPause.setSizePolicy(sizePolicy1)
        self.btnPause.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u"../imag/icons8_pause_26px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPause.setIcon(icon6)
        self.btnPause.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btnPause)

        self.btnStop = QPushButton(self.frmControls)
        self.btnStop.setObjectName(u"btnStop")
        sizePolicy1.setHeightForWidth(self.btnStop.sizePolicy().hasHeightForWidth())
        self.btnStop.setSizePolicy(sizePolicy1)
        self.btnStop.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u"../imag/icons8_stop_26px_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnStop.setIcon(icon7)
        self.btnStop.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.btnStop)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frmControls)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Youtube List Download", None))
#if QT_CONFIG(statustip)
        self.btnVideo.setStatusTip(QCoreApplication.translate("MainWindow", u"Descargar un video", None))
#endif // QT_CONFIG(statustip)
        self.btnVideo.setText("")
#if QT_CONFIG(statustip)
        self.btnLista.setStatusTip(QCoreApplication.translate("MainWindow", u"Descargar una lista", None))
#endif // QT_CONFIG(statustip)
        self.btnLista.setText("")
#if QT_CONFIG(statustip)
        self.btnTrash.setStatusTip(QCoreApplication.translate("MainWindow", u"Borrar descargas", None))
#endif // QT_CONFIG(statustip)
        self.btnTrash.setText("")
        self.btnConfig.setText("")
        ___qtablewidgetitem = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o", None));
        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None));
        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ETA", None));
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u" Comenzar", None))
        self.btnPause.setText(QCoreApplication.translate("MainWindow", u" Pausar", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u" Detener", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

