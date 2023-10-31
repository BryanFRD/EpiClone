from Colors import Colors


def print_success(str, replacable: bool = False) -> None:
    printr(Colors.OKGREEN + str, replacable)


def print_error(str, replacable: bool = False) -> None:
    printr(Colors.FAIL + str, replacable)


def printr(str, replacable: bool = False, endc: bool = True) -> None:
    print(str + Colors.ENDC if endc else "", end='\r' if replacable else '\n')


def print_ecp_logo():
    print("""
            ______      _ ________               
           / ____/___  (_) ____/ /___  ____  ___ 
          / __/ / __ \/ / /   / / __ \/ __ \/ _ \   
         / /___/ /_/ / / /___/ / /_/ / / / /  __/
        /_____/ .___/_/\____/_/\____/_/ /_/\___/ 
             /_/                                 
    """)


def print_info():
    print("\033[92mVersion: 1.0.0\033[0m")  # Show version with green color
    # Show info with colors
    print("\033[94mInformations:\033[0m")
    print(
        """EpiClone uses the GitHub API to retrieve all repositories from an organization, clones them to your computer and push to your github account.\n
        """
    )
    # add warning to use this project with caution and prerequisites
    print("\033[93mWarning:\033[0m")
    print(
        """This project is for educational purposes only. Please use it with caution and do not use it for malicious purposes.\n
        """
    )
    # add prerequisites
    print("\033[94mPrerequisites:\033[0m")
    print(
        """
        - Python 3.9
        - Github Account (https://github.com)
        - Github Token (https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)
        - Github Organization (https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch)
        - Github SSH Key (https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)
    """)

    print("\033[94mGitHub:\033[0m")
    print(
        """
        - Repository: github.com/BryanFRD/EpiClone
        - Contact: github.com/BryanFRD - github.com/ArthurAzoula
        - License: MIT
        - Contributors: BryanFRD - ArthurAzoula
    """)
