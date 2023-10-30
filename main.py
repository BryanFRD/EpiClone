from GitFolders import GitFolders

def __main__() -> None:
    gitFolders = GitFolders('/home/username')
    print(gitFolders.getGitFolders())


if __name__ == '__main__':
    __main__()
