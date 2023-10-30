import os

from Commands import Commands
from GithubApi import GithubApi
from GitFolders import GitFolders
from dotenv import load_dotenv

# load environment variables
load_dotenv()


def chooseMode():
    return input("Choose mode: \n1. Create new repositories from folders \n2. Clone repositories and create them from "
                 "Github url\n")


def foldersMode():
    folder_path = input("Enter folder path: ")
    gitFolders = GitFolders(folder_path)
    api = GithubApi(os.getenv('GITHUB_API_TOKEN'), os.getenv('GITHUB_USERNAME'))
    command = Commands(folder_path)
    for gitFolder in gitFolders.getGitFolders():
        if not api.checkIfRepositoryExists(gitFolder['name']):
            api.createNewRepository(gitFolder['name'])
            command.addOrigin(gitFolder['path'])
            command.push()


def cloneMode():
    # Get environment variables
    token = os.getenv('GITHUB_API_TOKEN') if os.getenv('GITHUB_API_TOKEN') else input("Enter your Github token: ")
    username = os.getenv('GITHUB_USERNAME') if os.getenv('GITHUB_USERNAME') else input("Enter your Github username: ")
    organizationName = input("Enter organization name: ")

    # Create GithubApi instance
    api = GithubApi(token, username)

    # Get all repositories from an organization
    repositories = api.getAllRepositoriesByAnOrganization(organizationName)

    # Get current folder
    current_folder = os.getcwd()

    # Create Commands instance
    commands = Commands(current_folder)

    # Create temp directory
    commands.createTempDirectory()

    # Create Commands instance for temp directory
    temp_directory = current_folder + "/temp"

    # Create Commands instance for temp directory
    command_temp = Commands(temp_directory)

    for repository in repositories:
        # Clone all repositories inside the temp folder
        command_temp.clone(repository['html_url'])

        # Add origin to all repositories inside the temp folder
        command_temp.addOrigin(repository['ssh_url'])

        # Push all repositories inside the temp folder
        command_temp.push()

    # Delete all repositories inside the temp folder
    commands.deleteFolder(temp_directory)
