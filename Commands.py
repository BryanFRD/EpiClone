import os
class Commands:

    def __init__(self, folder):
        self.folder = folder

    def clone(self, url) -> None:
        os.system(f"cd {self.folder} && git clone {url}")
        print(f"Cloned {url} to {self.folder}")

    def addOrigin(self, url) -> None:
        os.system(f"cd {self.folder} && git remote rm origin && git remote add origin {url}")
        print(f"Added origin {url}")

    def push(self) -> None:
        os.system(f"cd {self.folder} && git push --set-upstream origin main")
        print(f"Pushed to origin")

    def deleteFolder(self, folder) -> None:
        os.system(f"rm -rf {folder}")
        print(f"Deleted {folder}")

    def createTempDirectory(self):
        os.system(f"mkdir temp")
        print(f"Created temp directory")
