import os
from GithubApi import GithubApi
from GitFolders import GitFolders
from dotenv import load_dotenv

def __main__() -> None:
    load_dotenv()
    gitFolders = GitFolders('/home/username')
    api = GithubApi(os.getenv('GITHUB_API_TOKEN'), os.getenv('GITHUB_USERNAME'))
    for gitFolder in gitFolders.getGitFolders():
        if not api.checkIfRepositoryExists(gitFolder['name']):
            api.createNewRepository(gitFolder['name'])



    print(gitFolders.getGitFolders())


if __name__ == '__main__':
    __main__()
