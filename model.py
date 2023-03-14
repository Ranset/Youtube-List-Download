from pytube import YouTube, Playlist
from pySmartDL import SmartDL
from random import random
import os
import re
from urllib.parse import quote_plus
from time import sleep

class YouDownload:

    def segundos_a_segundos_minutos_y_horas(self, segundos):
        """Convert seconds to hours:minutes:seconds

        Args:
            segundos (int): Total leght in seconds ej: 125646

        Returns:
            str: String in format 00:00:00
        """
        horas = int(segundos / 60 / 60)
        segundos -= horas*60*60
        minutos = int(segundos/60)
        segundos -= minutos*60
        return f"{horas:02d}:{minutos:02d}:{segundos:02d}"    

    def video_info (self, url:str) -> object:
        """Return the video info from given url

        Args:
            url (str): The video's url
        """

        title = ""
        size = ""
        dwld_url = ""
        resolution = ""
        duration = ""

        try:
            yt = YouTube(url)
        except:
            print('Ah ocurrido un error. Revise la url del video')
            return ('Ah ocurrido un error. Revise la url del video',None,None,None,None)
        else:
            try:
                
                title = yt.title

                duration = self.segundos_a_segundos_minutos_y_horas(yt.length)
                
            except:
                print('No se pudo encontrar el video. Revise la conexión')
                return ('No se pudo encontrar el video. Revise la conexión',None,None,None,None)
            else:

                #Alternativa:
                #links = yt.streams.filter(progressive=True, res='720p')

                try:
                    # stream = yt.streams.get_highest_resolution()
                    stream = yt.streams.get_lowest_resolution()
                except:
                    print('No se pudo obtener link de descarga')
                    return ('No se pudo obtener link de descarga',None,None,None,None)
                else:
                    sizeMb = stream.filesize / 1000000

                    size = round(sizeMb,2)

                    resolution = stream.resolution

                    dwld_url = stream.url

                    return (title, size, duration, resolution, dwld_url, stream.subtype)
    
class VideoObjects:
    def __init__(self, id: int, video: tuple, path: str) -> None:
        self.title = video[0]
        self.size = video[1]
        self.duration = video[2]
        self.resolution = video[3]
        self.dwld_url = video[4]
        self.status = ''
        self.id = id
        self.path = path
        self.extension = video[5]

class TableDownload:

    def __init__(self, video_item: VideoObjects) -> None:
        self.video_item = video_item
        self.download_info = [video_item.id, "0%", '0', '0', '0', '']
        self.downloading = False

    def _rename(self, old:str, dest:str, filename:str, extention:str):
        new = dest + filename + '.' + extention
        try:
            os.rename(old, new)
        except FileExistsError:
            new = dest + filename + '_' + str(random()) + '.' + extention
            os.rename(old, new)

            print(new)

    def _clearString (self, string:str):
        regex = re.compile('[^0-9a-zA-Z&¡!{()}#$@,.óáéíñúüÁÉÍÓÚÜÑ]+')
        s = regex.sub(' ', string)
        return s

    def start (self) -> list:

        # dest = self.video_item.path.replace('\n','')
        dest = self.video_item.path.replace('/','\\') + '\\'

        obj = SmartDL(self.video_item.dwld_url, dest, progress_bar=False, timeout=15)
        obj.start(blocking=False)

        while not obj.isFinished():
            Velocidad = obj.get_speed(human=True)
            Descargado = obj.get_dl_size(human=True)
            Eta = obj.get_eta(human=True)
            Progreso = str(round(obj.get_progress()*100)) + '%'
            Estado = obj.get_status()
            self.download_info = [self.video_item.id, Progreso, Velocidad, Eta, Descargado, Estado]
            self.downloading = True
            sleep(0.2)

        if obj.isSuccessful:
            self.download_info[5] = 'Completado'

            self.downloading = False

            path = obj.get_dest()

            self._rename(path, dest, self._clearString(self.video_item.title), self.video_item.extension)

        else:
            print("Hubo un error durante la descrga:")
            for e in obj.get_errors():
                print(str(e))
    

if __name__ == "__main__":
    obj = YouDownload()
    result = obj.video_info('https://www.youtube.com/watch?v=V1WW1n0tEVM')
    print(result[0])