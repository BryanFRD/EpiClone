import os


def printr(message, color=Color.RESET):
    print(color + message + Color.RESET)


def get_github_token():
    token = os.getenv('GITHUB_API_TOKEN')
    if not token:
        token = input("Enter your Github token: ")
    while not token:
        printr("Github token is required.", Color.RED)
        token = input("Enter your Github token: ")
    return token


def get_github_username():
    username = os.getenv('GITHUB_USERNAME')
    if not username:
        username = input("Enter your Github username: ")
    while not username:
        printr("Github username is required.", Color.RED)
        username = input("Enter your Github username: ")
    return username


def get_organization_name():
    organization_name = input("Enter organization name: ")
    # Add any verification here if needed
    return organization_name


def get_folder_path():
    folder_path = input("Enter folder path: ")
    # Add any verification here if needed
    return folder_path


def get_mode():
    mode = input(
        "Choose mode: \n1. Create new repositories from folders \n2. Clone repositories and create them from Github URL\n")
    # Add verification for the mode selected (1 or 2)
    while mode not in ['1', '2']:
        printr("Invalid mode. Please choose 1 or 2.", Color.RED)
        mode = input(
            "Choose mode: \n1. Create new repositories from folders \n2. Clone repositories and create them from Github URL\n")
    return mode
