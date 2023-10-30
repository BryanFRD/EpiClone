from Colors import Colors

def print_success(str, replacable: bool = False) -> None:
    printr(Colors.OKGREEN + str, replacable)

def print_error(str, replacable: bool = False) -> None:
    printr(Colors.FAIL + str, replacable)

def printr(str, replacable: bool = False, endc: bool = True) -> None:
    print(str + Colors.ENDC if endc else "", end='\r' if replacable else '\n')