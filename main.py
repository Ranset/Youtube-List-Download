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
        # *************** videos de pruebas *** BORRAR *******
        url_a = 'https://rr4---sn-p5qs7nsk.googlevideo.com/videoplayback?expire=1679106956&ei=LM8UZPGoBomX_9EPyqu3kAo&ip=152.207.112.63&id=o-AJtaI54b08gL04tAOfbwc9NiewOKcHq90M5oEtoBtkvj&itag=18&source=youtube&requiressl=yes&mh=pF&mm=31%2C26&mn=sn-p5qs7nsk%2Csn-q4fzen7e&ms=au%2Conr&mv=m&mvi=4&pl=22&initcwndbps=37500&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=39.682&lmt=1672391663647811&mt=1679084941&fvip=4&fexp=24007246&c=ANDROID&txp=6219224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAIYmTxcouw-drdhW8xZjotAKdCVM75zEk-pJKGHNLcFoAiEA-PSJWJa4XLQZ9nt_JWckMa1IMk80LrAUfCpRI2miVkI%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAMohevLJMhuCNWXSUgWw4Bp_JJcj4U3_rvkbH7q5jV9lAiEAmE6ASL3mtI-Yw9AXQESZrS1nYOZZr3NEoxc3lDwKy6I%3D'
        url_b = 'https://rr1---sn-ab5sznzk.googlevideo.com/videoplayback?expire=1679107176&ei=CNAUZJGiFOuI_9EPraycmAs&ip=152.206.192.63&id=o-AIgIi1kfxgISL0BRpvk1HfB5dxuoqqaG1NkYTdkr7xC4&itag=18&source=youtube&requiressl=yes&mh=Sy&mm=31%2C29&mn=sn-ab5sznzk%2Csn-ab5l6nk6&ms=au%2Crdu&mv=m&mvi=1&pl=22&initcwndbps=92500&vprv=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=30.069&lmt=1645160442523171&mt=1679085184&fvip=3&fexp=24007246&c=ANDROID&txp=6218224&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIhALoxIobpQzq50P6OFRXdK_v9C_1SSeinPa7p5YWOWtckAiAfEfY0t4c_Ois2qYlhSKxzAnAtpWChiO2KvJJib7d6zQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAPHrAxHjxFSCNcRj49hJlA6h7iLdE6j95O7fffx0qCKcAiEAomobjEAbqnZdwyzxFrF4raW-yKQqUCqD3IZKHIQJPEk%3D'
        a = VideoObjects(1,('Video 1', 2.6, '00:00:22', '720p', url_a, 'mp4') ,'E:/TEMP')
        b = VideoObjects(0,('Video 2', 3.8, '00:00:40', '720p', url_b, 'mp4') ,'E:/TEMP')
        
        # url_a = 'https://www.egiptoexclusivo.com/wp-content/uploads/2022/08/historia-del-antiguo-egipto.jpg'
        # url_b = 'https://historia.nationalgeographic.com.es/medio/2018/02/27/paseo-por-egipto__1280x720.jpg'
        # a = VideoObjects(1,('Foto 1', 2.6, '00:00:22', '720p', url_a, 'jpg') ,'E:\TEMP')
        # b = VideoObjects(0,('Foto 2', 3.8, '00:00:40', '720p', url_b, 'jpg') ,'E:\TEMP')

        self.table_items.append(b)
        self.table_items.append(a)

        self.update_table()

        #************************************************


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

    def clear_table (self):
        while self.gui.table.rowCount() > 0:
            self.gui.table.removeRow(0)

    def update_table (self):
        # Limpiamo la tabla
        self.clear_table()

        for item in self.table_items:
            # Insertamos una row debajo de todas
            self.gui.table.insertRow(item.id)

            # Agregamos elementos a la fila
            self.gui.table.setItem(item.id, 0, QTableWidgetItem(item.title))
            self.gui.table.setItem(item.id, 1, QTableWidgetItem(str(item.size)+'MB'))
            self.gui.table.item(item.id,1).setTextAlignment(132) # 132 alinea al centro y 130 a la derecha
            self.gui.table.setItem(item.id, 2, QTableWidgetItem(item.status))
            self.gui.table.item(item.id,2).setTextAlignment(132) # 132 alinea al centro y 130 a la derecha
            self.gui.table.setItem(item.id, 3, QTableWidgetItem(''))
            self.gui.table.setItem(item.id, 4, QTableWidgetItem(''))

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
                    try:
                        resultado = download.start()
                    except Exception as e:
                        print(e)
                        self.gui.btnStart.setEnabled(True)
                        self.table_items[video.id].status = 'Error'
                        self.update_table()
                    else:
                        print(resultado)
                        self.table_items[video.id].status = resultado[5]
                        self.update_table()
            print('Todas las descargas finalizadas')
            self.downloading = False
            self.gui.btnStart.setEnabled(True)

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
        self.gui.btnTrash.clicked.connect(lambda: self.clear_table())

        self.gui.btnStart.clicked.connect(self.start_download)
        
        # [End_Eventos]

if __name__ == "__main__":
    win = Qmain()
    win.eventListener()
    win.on_load()
    win.run()