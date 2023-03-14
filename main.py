# Views (uis)
import ui_main as ui
import ui_dlgDownloadVideo as dlgVideo
import ui_dlgDownloadList as dlgList
import ui_dlgConfig as dlgConfig
import ui_dlgAbout as About

import sys
import json
import threading
from time import sleep
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QMenu, QFileDialog, QTableWidgetItem
from model import YouDownload, VideoObjects, TableDownload

class Qmain:
    #[Atributos Globales]
    ruta : str
    table_items = []
    num_item = 0
    downloading = False
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

    def update_table (self):
        # Limpiamo la tabla
        while self.gui.table.rowCount() > 0:
            self.gui.table.removeRow(0)

        for item in self.table_items:
            # Insertamos una row debajo de todas
            self.gui.table.insertRow(item.id)

            # Agregamos elementos a la fila
            self.gui.table.setItem(item.id, 0, QTableWidgetItem(item.title))
            self.gui.table.setItem(item.id, 1, QTableWidgetItem(str(item.size)+'MB'))
            self.gui.table.item(item.id,1).setTextAlignment(132) # 132 alinea al centro y 130 a la derecha

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

        self.video : VideoObjects
        # rowPosition = self.gui.table.rowCount()
        self.isSecondGet = False

        # Buttons Events
        gui.btnAgregar.clicked.connect(lambda: add_file_to_table()) # Agregar
        gui.btnCancel.clicked.connect(lambda: close_dlgVideo ()) # Cancel
        

        def add_file_to_table ():
            self.table_items.append(self.video)
            self.update_table()
            dialog1.close()

        def get_video_info ():
            self.isSecondGet = True
            url = gui.lineEdit.text()
            ytd = YouDownload()
            gui.lblVideoName.setText('Obteniendo video...')
            video_info = ytd.video_info(url)
            self.video = VideoObjects(self.num_item, video_info, self.ruta)
            self.num_item += 1
            gui.lblVideoName.setText(self.video.title)
            gui.label_5.setText(self.video.duration)
            gui.label_6.setText(str(self.video.size) + 'MB')
            gui.label_7.setText(self.video.path)
            gui.btnAgregar.setEnabled(True)
            
        t1 = threading.Thread(target=get_video_info, daemon=True)
        # gui.btnGet.clicked.connect(lambda: t1.run() if self.isSecondGet else t1.start()) # Get. Lambda comprueba si es la primera o segunda vez que se llama al thread... value_when_true if condition else value_when_false
        gui.btnGet.clicked.connect(lambda: t1.start()) # Get

        def close_dlgVideo ():
            dialog1.close()
        
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

    def trash (self):
        video = VideoObjects(self.num_item, ('Video Test', 10, '00:00:00', '720', 'htttpmbmdnabmdamnd'), self.ruta)
        self.num_item += 1
        self.table_items.append(video)
        self.update_table()


    def start_download (self):
        self.downloading = True
        self.gui.btnStart.setEnabled(False)
        self.download_obj : TableDownload
        self.id = 0

        def download ():
            for video in self.table_items:
                if video.status == 'Completado':
                    break
                else:
                    self.id = video.id
                    download = TableDownload(video)
                    self.download_obj = download
                    download.start()

        t2 = threading.Thread(target=download, daemon=True)
        t2.start()

        def get_download_info ():
            while self.downloading:
                info = self.download_obj.download_info
                if self.download_obj.downloading:
                    # print(self.download_obj.download_info)
                    self.gui.table.setItem(info[0], 2, QTableWidgetItem(str(info[1])))
                    self.gui.table.item(info[0], 2).setTextAlignment(132) # 132 alinea al centro y 130 a la derecha
                    self.gui.table.setItem(info[0], 3, QTableWidgetItem(str(info[2])))
                    self.gui.table.item(info[0], 3).setTextAlignment(132) # 132 alinea al centro y 130 a la derecha
                    self.gui.table.setItem(info[0], 4, QTableWidgetItem(str(info[3])))
                    self.gui.table.item(info[0], 4).setTextAlignment(132) # 132 alinea al centro y 130 a la derecha
                    self.table_items[info[0]].status = self.download_obj.download_info[5]
                elif info[5] == 'Completado':
                    self.gui.table.setItem(info[0], 2, QTableWidgetItem('Completado'))
                    self.gui.table.item(info[0], 2).setTextAlignment(132) # 132 alinea al centro y 130 a la derecha
                    self.gui.table.setItem(info[0], 3, QTableWidgetItem(''))
                    self.gui.table.setItem(info[0], 4, QTableWidgetItem(''))
                else:
                    self.gui.table.setItem(info[0], 2, QTableWidgetItem('Iniciando...'))
                    self.gui.table.item(info[0], 2).setTextAlignment(132) # 132 alinea al centro y 130 a la derecha
                sleep(0.5)

        t3 = threading.Thread(target=get_download_info, daemon=True)
        t3.start()


    #[END metodos]

    def eventListener (self):
        #[Eventos]
        self.gui.btnVideo.clicked.connect(self.open_dlgVideo)
        self.gui.btnLista.clicked.connect(self.open_dlgList)
        self.gui.btnTrash.clicked.connect(self.trash)

        self.gui.btnStart.clicked.connect(self.start_download)
        
        # [End_Eventos]

if __name__ == "__main__":
    win = Qmain()
    win.eventListener()
    win.on_load()
    win.run()