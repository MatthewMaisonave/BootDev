#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
#from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test_run():
    test_a = run_python_file("calculator", "main.py") 
    test_b = run_python_file("calculator", "main.py", ["3 + 5"]) 
    test_c = run_python_file("calculator", "tests.py")
    test_d = run_python_file("calculator", "../main.py") 
    test_e = run_python_file("calculator", "nonexistent.py")
    test_f = run_python_file("calculator", "lorem.txt")

    print(f"Result for main.py:\n{test_a}")
    print(f"Result for main.py:\n{test_b}")
    print(f"Result for tests.py:\n{test_c}")
    print(f"Result for main.py:\n{test_d}")
    print(f"Result for nonexsistent.py:\n{test_e}")
    print(f"Result for lorem.txt:\n{test_f}")

"""
def test_write():
    test_a = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    test_b = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    test_c = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

    print(f"Result for lorem.txt:\n{test_a}")
    print(f"Result for 'pkg/morelorem.txt' file:\n{test_b}")
    print(f"Result for '/tmp/temp.txt' directory:\n{test_c}")


def test_content():
    test_a = get_file_content("calculator", "main.py")
    test_b = get_file_content("calculator", "pkg/calculator.py")
    test_c = get_file_content("calculator", "/bin/cat")
    test_d = get_file_content("calculator", "pkg/does_not_exist.py")

    print(f"Result for main.py file:\n{test_a}")
    print(f"Result for 'pkg/calculator.py' file:\n{test_b}")
    print(f"Result for '/bin/cat' directory:\n{test_c}")
    print(f"Result for 'pkg/does_not_exist.py' file:\n{test_d}")


def test_info():
    test_a = get_files_info("calculator", ".")
    test_b = get_files_info("calculator", "pkg")
    test_c = get_files_info("calculator", "/bin")
    test_d = get_files_info("calculator", "../")

    print(f"Result for current directory:\n{test_a}")
    print(f"Result for 'pkg' directory:\n{test_b}")
    print(f"Result for '/bin' directory:\n{test_c}")
    print(f"Result for '../' directory:\n{test_d}")

"""
if __name__ == "__main__":
    #test_info()
    #test_content()
    #test_write()
    test_run()