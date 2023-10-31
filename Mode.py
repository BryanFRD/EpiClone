import os

from Commands import Commands
from GithubApi import GithubApi
from GitFolders import GitFolders
from dotenv import load_dotenv
from Inputs import *
import datetime

# load environment variables
load_dotenv()

def chooseMode():
    return get_mode()


def foldersMode():
    folder_path = get_folder_path()
    gitFolders = GitFolders(folder_path)
    api = GithubApi(os.getenv('GITHUB_API_TOKEN'), os.getenv('GITHUB_USERNAME'))
    command = Commands(folder_path)
    for gitFolder in gitFolders.getGitFolders():
        if not api.checkIfRepositoryExists(gitFolder['name']):
            api.createNewRepository(gitFolder['name'])
            command.addOrigin(gitFolder['path'])
            command.push()
            command.removeOrigin()


def cloneMode():
    # Get environment variables
    token = get_github_token()
    username = get_github_username()
    organizationName = get_organization_name()

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
        command_temp.clone(repository['ssh_url'])
        repository_updated_at = datetime.date(repository['updated_at'])

        # Check if repository exists and create it if it doesn't
        if not api.checkIfRepositoryExists(repository['name']):
            api.createNewRepository(repository['name'])

        command_repo = Commands(temp_directory + "/" + repository['name'])
        git_folder = GitFolders(temp_directory + "/" + repository['name'])

        github_repo_updated_at = datetime.datetime(api.getRepository(repository['name']))

        if github_repo_updated_at >= repository_updated_at:
            continue

        if not git_folder.isEmpty():
            # Add origin to all repositories inside the temp folder
            command_repo.addOrigin(f"git@github.com:{username}/{repository['name']}.git")

            # Push all repositories inside the temp folder
            command_repo.push()

        # Delete repository inside the temp folder
        command_repo.deleteFolder(temp_directory + "/" + repository['name'])

    # Delete all repositories inside the temp folder
    commands.deleteFolder(temp_directory)
