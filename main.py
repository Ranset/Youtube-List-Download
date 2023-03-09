# Views (uis)
import ui_main as ui
import ui_dlgDownloadVideo as dlgVideo
import ui_dlgDownloadList as dlgList
import ui_dlgConfig as dlgConfig
import ui_dlgAbout as About

import sys
import json
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMenu, QFileDialog, QTableWidgetItem
from model import YouDownload

class Qmain:
    #[Atributos Globales]
    ruta : str
    #[End_Atributos Globales]

    def __init__(self) -> None:
        self.app = ui.QApplication(sys.argv)
        MainWindow = ui.QMainWindow()
        self.main = MainWindow
        gui = ui.Ui_MainWindow()
        gui.setupUi(MainWindow)
        self.gui = gui

    def run (self):
        self.main.show()
        sys.exit(self.app.exec_())

    #[metodos]
    def on_load(self):
        """Ejecute when main windows load
        """

        # Cargamos la configuracion del json
        with open ('./config.json', 'r') as f:
            config = json.load(f)
            self.ruta = config['ruta']

        #Menu context
        self.menu = QMenu()
            #Add menu actions
        self.menu.addAction("Configuración", self.open_config)
        self.menu.addAction("Acerca de...", self.open_about)

            #Add context menu to button
        self.gui.btnConfig.setMenu(self.menu)

        # End Menu context

        # Tamaño de la columna 1
        self.gui.table.setColumnWidth(0, 220)

    def open_config(self):
        """Open download Config dialog"""
        app = dlgConfig.QThread()
        dialog = dlgConfig.QDialog()
        gui = dlgConfig.Ui_Dialog()
        gui.setupUi(dialog)

        # Cargar la url de la carpeta en el input
        gui.lineEdit.setText(self.ruta)

        # Buttons Events
        gui.btnFolder.clicked.connect(lambda: select_folder()) # Select directory
        gui.btnAceptar.clicked.connect(lambda: aceptar_config_dlg()) # Aceptar

        def select_folder ():
            folder = QFileDialog.getExistingDirectory()
            gui.lineEdit.setText(folder)

        def aceptar_config_dlg ():
            self.ruta = gui.lineEdit.text()

            # Salvando ruta de guardado al json
            with open ('./config.json', 'w') as f:
                obj = {'ruta' : self.ruta}
                json.dump(obj, f)

            dialog.close()

        dialog.show()
        sys.exit(app.exec_())

    def open_about(self):
        """Open about dialog"""
        app = About.QThread()
        dialog = About.QDialog()
        gui = About.Ui_Dialog()
        gui.setupUi(dialog)

        dialog.show()
        sys.exit(app.exec_())

    def open_dlgVideo (self):
        """Open download video dialog"""
        app2 = dlgVideo.QThread()
        dialog1 = dlgVideo.QDialog()
        gui = dlgVideo.Ui_frmDownVideo()
        gui.setupUi(dialog1)

        self.video_info : tuple

        # Buttons Events
        gui.btnAgregar.clicked.connect(lambda: add_file_to_table()) # Agregar
        gui.btnCancel.clicked.connect(lambda: dialog1.close()) # Cancel
        gui.btnGet.clicked.connect(lambda: get_video_info()) # Get

        def add_file_to_table ():
            # Insertamos una row debajo de todas
            rowPosition = self.gui.table.rowCount()
            self.gui.table.insertRow(rowPosition)

            # Agregamos elementos a la fila
            self.gui.table.setItem(rowPosition, 0, QTableWidgetItem(gui.lblVideoName.text()))
            self.gui.table.setItem(rowPosition, 1, QTableWidgetItem(gui.label_6.text()))
            self.gui.table.item(rowPosition,1).setTextAlignment(132) # 132 alinea al centro y 130 a la derecha

        def get_video_info ():
            url = gui.lineEdit.text()
            ytd = YouDownload()
            self.video_info = ytd.video_info(url)
            print(self.video_info) # Borrar
            gui.lblVideoName.setText(self.video_info[0])
            gui.label_5.setText(self.video_info[2])
            gui.label_6.setText(str(self.video_info[1]) + 'MB')
            gui.label_7.setText(self.ruta)
            gui.btnAgregar.setEnabled(True)
        
        dialog1.show()
        sys.exit(app2.exec_())

    def open_dlgList (self):
        """Open download list dialog"""
        app2 = dlgList.QThread()
        dialog = dlgList.QDialog()
        gui = dlgList.Ui_frmDownList()
        gui.setupUi(dialog)

        # Buttons Events
        gui.pushButton_3.clicked.connect(lambda: dialog.close()) # Cancel

        dialog.show()
        sys.exit(app2.exec_())

    #[END metodos]

    def eventListener (self):
        #[Eventos]
        self.gui.btnVideo.clicked.connect(self.open_dlgVideo)
        self.gui.btnLista.clicked.connect(self.open_dlgList)
        
        # [End_Eventos]

if __name__ == "__main__":
    win = Qmain()
    win.eventListener()
    win.on_load()
    win.run()