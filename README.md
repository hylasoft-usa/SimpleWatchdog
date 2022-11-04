# Python Watchdog
## Use
Monitors a directory for changes, prints all changes to a log file
### Configuration
Edit the WatchDogConfig.ini file to change paths of monitored directory or logfile location. By default the application logs to the same folder it is run from:
DirToMonitor = The directory to monitor for file changes
LogfileLocation = Fully qualified location of the log file, including the name and extension (C:/testLogfile.txt as an example)
###Running the application
After configuring the settings, simply run the WatchDog.exe located in the Dist folder
### Building the application
If changes are made to the python script, re run the "CreatePackage.bat" file
