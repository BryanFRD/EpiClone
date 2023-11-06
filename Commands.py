import os
import sys
from PrintHelper import *
class Commands:

    _origin = "epitech_clone_project"

    def __init__(self, folder):
        self.folder = folder

    def clone(self, url) -> None:
        # change if it's Windows
        if sys.platform == 'win32' or sys.platform == 'win64':
            os.system(f"cd {self.folder} && git clone {url} --quiet >nul 2>&1")
        else:
            os.system(f"cd {self.folder} && git clone {url} --quiet 2>/dev/null")


    def addOrigin(self, url) -> None:
        os.system(f"cd {self.folder} && git remote add {self._origin} {url}")
        #print(f"Added origin {url}")

    def removeOrigin(self) -> None:
        os.system(f"cd {self.folder} && git remote rm {self._origin}")
        #print(f"Removed origin")

    def push(self, branch: str = 'main') -> None:
        os.system(f"cd {self.folder} && git push {self._origin} {branch} --quiet")
        #print_success(f"Pushed to {self._origin}")

    def checkIfFolderExists(self, folder) -> bool:
        return os.path.isdir(folder)

    def deleteFolder(self, folder) -> None:
        if sys.platform == 'win32' or sys.platform == 'win64':
            os.system(f"rmdir /s /q {folder}")
        else:
            os.system(f"rm -rf {folder}")
        #print(f"Deleted {folder}")

    def createTempDirectory(self):
        os.system(f"mkdir temp")
        #print(f"Created temp directory")

    def clearTerminal(self):
        os.system("clear")
        #print(f"Cleared terminal")
