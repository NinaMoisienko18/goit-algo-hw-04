import sys
from pathlib import Path
from colorama import Fore, Style

def display_directory_structure(directory_path):
        path = Path(directory_path)
        print(Fore.GREEN + f"Directory structure for {path.name}:\n" + Style.RESET_ALL)
        display_contents(path)

        if not path.exists():
            print(Fore.RED + "Path does not exist.")



def display_contents(path, count=0):
    for i in path.iterdir():
        if i.is_dir():
            print("\t" * count + Fore.YELLOW + f"📁 {i.name}" + Style.RESET_ALL)
            display_contents(i, count + 1)

        elif i.is_file():
            print("\t" * count + Fore.CYAN + f"📄 {i.name}" + Style.RESET_ALL)


def main():
    directory_path = sys.argv[1]
    display_directory_structure(directory_path)

if __name__ == "__main__":
    main()
