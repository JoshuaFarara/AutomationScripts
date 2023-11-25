import os
import pythoncom
from win32com.client import Dispatch

def create_shortcut(target_path, shortcut_path, working_directory=None, shortcut_key=None):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path

    if working_directory:
        shortcut.WorkingDirectory = working_directory

    if shortcut_key:
        shortcut.Hotkey = shortcut_key

    shortcut.Save()

# Example usage:
batch_file_path = 'C:\\Users\\User\\Desktop\\AutomationScripts\\Workflows\\Batch\\runscript_100DayC.bat'
shortcut_path = 'C:\\Users\\User\\Desktop\\runscript_100DayC.lnk'
working_dir = 'C:\\Users\\User\\Desktop\\AutomationScripts\\Workflows\\Batch'

user_shortcut_key = input("Enter the shortcut key combination (e.g., Ctrl+Alt+F): ")

create_shortcut(batch_file_path, shortcut_path,  working_directory=working_dir, shortcut_key=user_shortcut_key)