from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
from functions.write_files import write_file
from functions.run_python_file import run_python_file

def main():
    working_directory = "."
    print(run_python_file(working_directory, "calculator/main.py", ["3 + 5"]))
 
main()