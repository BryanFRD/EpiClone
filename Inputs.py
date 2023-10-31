import os
from Colors import Colors  # Assuming Colors module exists with color definitions


def printr(message, color=Colors.UNDERLINE):
    print(color + message + Colors.ENDC)  # Use ENDC to reset terminal color


def get_github_token():
    token = os.getenv('GITHUB_API_TOKEN')
    if not token:
        printr("Please enter your Github token: ", Colors.BOLD)
        token = input()
    while not token:
        printr("Github token is required.", Colors.FAIL)
        printr("Please enter your Github token: ", Colors.BOLD)
        token = input()
    return token


def get_github_username():
    username = os.getenv('GITHUB_USERNAME')
    if not username:
        printr("Please enter your Github username: ", Colors.BOLD)
        username = input()
    while not username:
        printr("Github username is required.", Colors.FAIL)
        printr("Please enter your Github username: ", Colors.BOLD)
        username = input()
    return username


def get_organization_name():
    organization_name = input("Enter organization name (EpitechMscProPromo2026): ")
    if not organization_name:
        return 'EpitechMscProPromo2026'
    return organization_name


def get_folder_path():
    folder_path = input("Enter folder path [ /home/username ]: ")
    if not folder_path:
        printr("Folder path is required.", Colors.FAIL)
        printr("Please enter the folder path [ /home/username ]: ", Colors.BOLD)
        folder_path = input()
    return folder_path


def get_mode():
    printr("Choose mode: ", Colors.BOLD)
    print("1. Create new repositories from folders")
    print("2. Clone repositories and create them from Github URL")
    mode = input()
    while mode not in ['1', '2']:
        printr("Invalid mode. Please choose 1 or 2.", Colors.FAIL)
        printr("Choose mode: ", Colors.BOLD)
        print("1. Create new repositories from folders")
        print("2. Clone repositories and create them from Github URL")
        mode = input()
    return mode
