#!/bin/python3.8

import feedparser
import urllib.request
import os
import time

# URL de la lista RSS en XML
#rss_url = "http://www.locafm.com/podcast/la-termo__dj-neil.xml"
rss_url = "http://www.locafm.com/podcast/la-termo__dj-neil.xml"

# Carpeta donde se guardarán los archivos mp3
download_folder = "/volume1/14Teras/Multimedia/Musica/Sesiones/LocaFM/La_Termo/"

# Tiempo máximo (en segundos) que se considerará un archivo como "nuevo"
max_age = 86400 * 30 # 30 días

# Parsear el feed RSS
feed = feedparser.parse(rss_url)

# Iterar a través de las entradas del feed
for entry in feed.entries:
    # Obtener el enlace de descarga del archivo mp3
    mp3_url = entry.enclosures[0].href
    
    # Obtener el nombre del archivo mp3
    mp3_name = mp3_url.split("/")[-1]
    
    # Verificar si el archivo ya existe en la carpeta de descarga
    if os.path.exists(download_folder + mp3_name):
        # Obtener la fecha de modificación del archivo existente
        file_age = time.time() - os.path.getmtime(download_folder + mp3_name)
        
        # Si el archivo es más nuevo que el tiempo máximo, no se descarga de nuevo
        if file_age < max_age:
            print("Archivo ya existe:", mp3_name)
            continue
    
    # Descargar el archivo mp3
    urllib.request.urlretrieve(mp3_url, download_folder + mp3_name)
    
    # Imprimir el nombre del archivo descargado
    print("Descargado:", mp3_name)
    
    # Eliminar los archivos más antiguos de un mes
    for file in os.listdir(download_folder):
        if file.endswith(".mp3"):
            file_age = time.time() - os.path.getmtime(download_folder + file)
            if file_age > max_age:
                os.remove(download_folder + file)
                print("Eliminado:", file)
