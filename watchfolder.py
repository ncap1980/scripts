import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            remove_metadata(file_path)

def remove_metadata(file_path):
    try:
        subprocess.run(['exiftool', '-all=', file_path], check=True)
        print(f"Metadatos eliminados de {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error eliminando metadatos de {file_path}: {e}")

if __name__ == '__main__':
    folder_path = input("Introduce la ruta del directorio a vigilar: ")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    print(f"Vigilando el directorio {folder_path}...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()