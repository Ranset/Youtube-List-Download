from pytube import YouTube, Playlist
from pySmartDL import SmartDL
from random import random
import os
import re
from urllib.parse import quote_plus

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

    def video_info (self, url:str) -> tuple:
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
        else:
            try:
                
                title = yt.title

                duration = self.segundos_a_segundos_minutos_y_horas(yt.length)
                
            except:
                print('No se pudo encontrar el video. Revise la conexión')
            else:

                #Alternativa:
                #links = yt.streams.filter(progressive=True, res='720p')

                try:
                    stream = yt.streams.get_highest_resolution()
                except:
                    print('No se pudo obtener link de descarga')
                else:
                    sizeMb = stream.filesize / 1000000

                    size = round(sizeMb,2)

                    resolution = stream.resolution

                    dwld_url = stream.url

                    return (title, size, duration, resolution, dwld_url)
    
if __name__ == "__main__":
    obj = YouDownload()
    result = obj.video_info('https://www.youtube.com/watch?v=V1WW1n0tEVM')
    print(result[0])