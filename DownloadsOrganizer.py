import os
from pathlib import Path
import shutil


directories = {
    "Pictures Folder": [".jpeg", ".jpg", ".gif", ".png"],
    "Videos Folder": [".wmv", ".mov", ".mp4", ".mpg", ".mpeg", ".mkv"],
    "ZIP Folder": [".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".zip"],
    "Music Folder": [".mp3", ".msv", ".wav", ".wma"],
    "PDF Folder": [".pdf"],
    "Docs Folder": [".docx"],
    "Executables": [".exe", ".msi"]
}


def get_downloads_path():
    if os.name == "nt":
        import winreg
        reg_key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")

        downloads_path = winreg.QueryValueEx(
            reg_key, "{374DE290-123F-4565-9164-39C4925E467B}")[0]

        winreg.CloseKey(reg_key)

        return downloads_path


def create_directories():
    for directory in directories:

        currentDirectory = get_downloads_path() + '\\' + directory

        if not os.path.exists(currentDirectory):
            print("Folder does not exist. Creating folder...")
            os.makedirs(currentDirectory)
        else:
            print(directory + " found.")

    if not os.path.exists(get_downloads_path() + '\\Others'):
        print("Folder does not exist. Creating folder...")
        os.makedirs(get_downloads_path() + '\\Others')
    else:
        print("Others found.")


def getDirectoryMatch(file):
    filename, extension = os.path.splitext(file)
    for directory in directories:
        for availableExtension in directories[directory]:
            if extension == availableExtension:
                return directory
    return False


def file_organizer(files):
    print("Organizing files...")

    for file in files:
        # print(file)
        if not os.path.isfile(get_downloads_path() + "\\" + file) or file == "desktop.ini":
            continue
        if file == os.path.basename(__file__):
            continue

        directory = getDirectoryMatch(file)
        if directory != False:
            shutil.move(get_downloads_path() + '\\' + file,
                        get_downloads_path() + '\\' + directory)

        else:
            shutil.move(get_downloads_path() + '\\' + file,
                        get_downloads_path() + '\\Others')

    print("Done.")


create_directories()

files = os.listdir(get_downloads_path())
file_organizer(files)
