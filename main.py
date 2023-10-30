from Mode import *


def __main__() -> None:
    mode = chooseMode()

    if mode == "1":
        foldersMode()
    elif mode == "2":
        cloneMode()
    else:
        print("Invalid mode")


if __name__ == '__main__':
    __main__()
