import os
class Commands:

    _remote = "epitech_clone_project"

    def __init__(self, folder):
        self.folder = folder

    def clone(self, url) -> None:
        os.system(f"git clone {url} {self.folder}")
        print(f"Cloned {url} to {self.folder}")

    def addOrigin(self, url) -> None:
        os.system(f"cd {self.folder} && git remote add {self._remote} {url}")
        print(f"Added origin {url}")

    def push(self) -> None:
        os.system(f"cd {self.folder} && git push {self._remote} main")
        print(f"Pushed to origin")

    def deleteFolder(self, folder) -> None:
        os.system(f"rm -rf {folder}")
        print(f"Deleted {folder}")

    def createTempDirectory(self):
        os.system(f"mkdir temp")
        print(f"Created temp directory")