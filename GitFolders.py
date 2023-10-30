import os


class GitFolders:

    def __init__(self, rootFolder) -> None:
        self.rootFolder = rootFolder

    def getGitFolders(self):
        gitFolders = []
        for root, dirs, files in os.walk(self.rootFolder):
            if '.git' in dirs:
                gitFolders.append({
                    'name': root.split('/')[-1],
                    'path': root
                })
        return gitFolders
