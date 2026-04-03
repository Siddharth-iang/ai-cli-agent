from operator import ge
from webbrowser import get
from functions.get_files_info import get_files_info

def main():
    print(get_files_info("calculator"))
    root_contents = get_files_info(working_directory=".")
    print(root_contents)
    pkg_contents = get_files_info(working_directory=".", directory="pkg")
    print(pkg_contents)
    pkg_contents = get_files_info(working_directory=".", directory="../")
    print(pkg_contents)