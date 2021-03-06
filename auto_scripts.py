from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        i = 1
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(folder_destination + r"\" + new_name)
            while file_exists:
                self.i += 1
                new_name = "new_file_" + str(self.i) + ".txt"
                file_exists = os.path.isfile(folder_destination + r"\" + new_name)

            src = folder_to_track + r"\" + filename
            new_destination = folder_destination + r"\" + filename
            os.rename(src, new_destination)

folder_to_track = r"C:\Users\Rado\Desktop\myFolder"
folder_destination = r"C:\Users\Rado\Desktop\new"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

