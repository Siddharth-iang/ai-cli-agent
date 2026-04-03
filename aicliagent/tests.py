from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
from functions.write_files import write_file

def main():
    working_directory = "calculator"
    # print(write_file("calculator", "lorem.txt", "Wait, this is a test file."))
    # print(write_file("calculator", "pkg/lorem2.txt", "Wait, this is a another test file."))
    print(write_file("calculator", "pkg2/temp.txt", "this should be allowed"))
 
main()