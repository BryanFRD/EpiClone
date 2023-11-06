import os
import sys

from Commands import Commands
from GithubApi import GithubApi
from GitFolders import GitFolders
from dotenv import load_dotenv
from Inputs import *
import datetime
from alive_progress import alive_bar
from tqdm import tqdm

from PrintHelper import *

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
    # print logo and info about the project
    print_ecp_logo()
    print_info()

    separator = "\\" if sys.platform == 'win32' or sys.platform == 'win64' else "/"

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

    # clear terminal
    commands.clearTerminal()

    if commands.checkIfFolderExists("temp"):
        commands.deleteFolder("temp")

    # Create temp directory
    commands.createTempDirectory()

    # Create Commands instance for temp directory
    temp_directory = current_folder + f"{separator}temp"

    # Create Commands instance for temp directory
    command_temp = Commands(temp_directory)

    cloned_repositories = 0
    pushed_repositories = 0

    with tqdm(total=len(repositories), desc="Starting clone", unit="repo") as pbar_total:
        for repository in repositories:
            pbar_total.set_description(f"{Colors.OKGREEN}[{repository['name']}] {Colors.ENDC} Cloning repository",
                                       True)

            # Update the total progress bar for each repository cloned
            pbar_total.update(1)

            # Check if repository exists and create it if it doesn't
            if not api.checkIfRepositoryExists(repository['name']):
                api.createNewRepository(repository['name'])

            if '--force' not in sys.argv and not api.isDifferent(repository):
                continue

            command_repo = Commands(temp_directory + separator + repository['name'])
            git_folder = GitFolders(temp_directory + separator + repository['name'])

            if '--force' not in sys.argv and not api.isDifferent(repository):
                continue

            # Clone all repositories inside the temp folder
            command_temp.clone(repository['ssh_url'])

            cloned_repositories += 1

            if command_temp.checkIfFolderExists(repository['name']) and not git_folder.isEmpty():
                pbar_total.set_description(f"{Colors.OKGREEN}[{repository['name']}] {Colors.ENDC} Pushing repository", True)

                # Add origin to all repositories inside the temp folder
                command_repo.addOrigin(f"git@github.com:{username}/{repository['name']}.git")

                # Push all repositories inside the temp folder
                command_repo.push(repository['default_branch'])

                pushed_repositories += 1

            # Delete repository inside the temp folder
            command_repo.deleteFolder(temp_directory + separator + repository['name'])

    # Delete all repositories inside the temp folder
    commands.deleteFolder(temp_directory)

    print_success("All repositories have been cloned successfully!")
    print_success(f"Pushed {pushed_repositories} repositories out of {cloned_repositories} cloned repositories.")
