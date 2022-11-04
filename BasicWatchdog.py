# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 09:12:03 2022

@author: psieb
"""

import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from configparser import ConfigParser

config_object = ConfigParser();
config_object.read("WatchDogConfig.ini");
settings = config_object["BasicSettings"];

MonitorPath = settings["DirToMonitor"]
LogPath = settings["LogfileLocation"] 
print(MonitorPath)
print(LogPath)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        filename=LogPath,
                        filemode='a',
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path=MonitorPath;
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)  #Scheduling monitoring of a path with the observer instance and event handler. There is 'recursive=True' because only with it enabled, watchdog.observers.Observer can monitor sub-directories
    observer.start()  #for starting the observer thread
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()