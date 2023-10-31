from Colors import Colors


def print_success(str, replacable: bool = False) -> None:
    printr(Colors.OKGREEN + str, replacable)


def print_error(str, replacable: bool = False) -> None:
    printr(Colors.FAIL + str, replacable)


def printr(str, replacable: bool = False, endc: bool = True) -> None:
    print(str + Colors.ENDC if endc else "", end='\r' if replacable else '\n')

def print_ecp_logo():
    print(""" 
        _______   ________  ________   
        |\  ___ \ |\   ____\|\   __  \  
        \ \   __/|\ \  \___|\ \  \|\  \ 
         \ \  \_|/_\ \  \    \ \   ____\    
          \ \  \_|\ \ \  \____\ \  \___|
           \ \_______\ \_______\ \__\   
            \|_______|\|_______|\|__|   
    """)

def print_info():
    print("\033[92mVersion: 1.0.0\033[0m")  # Show version with green color
    # Show info with colors
    print("\033[94mInformations:\033[0m")
    print(
        """This project uses the GitHub API to retrieve all repositories from an organization, clones them to your computer and push to your github account.\n"""
    )
    print("\033[94mGitHub:\033[0m")
    print(
        """
        - Repository: github.com/BryanFRD/EpitechCloneProject
        - Contact: github.com/BryanFRD - github.com/ArthurAzoula
        - License: MIT
        - Contributors: BryanFRD - ArthurAzoula
    """)

