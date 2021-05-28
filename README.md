# universal-runpp
A script that compiles and runs any file with notepad++ based on its extension. Currently supported languages are Python, Javascript, and Java, but I plan to make it an plugin for Notepad++ that can run anything.

# Usage
Download the script file run.py, place it anywhere you want, I prefer to use the Notepad++ installation path. Open Notepad++, select Run->Run... from the menu bar. Enter the following into the menu that pops up: `path/to/run.py" "$(FULL_CURRENT_PATH)"` making sure to replace `path/to/run.py` with the actual path where you placed run.py. Then, click save and choose a shorcut and a name for the command. Now if you press the shortcut the script should run the appropriate file and pause on exit.

