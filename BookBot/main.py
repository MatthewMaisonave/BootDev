from stats import get_word_count, char_occurrnce, dict_sort
import sys

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def output_bookbot(path, word_count, sorted_list):
    print("============ BOOKBOT ============\n"+ 
          f"Analyzing book found at {path}...\n"+ 
          "----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        char = str(dict["char"])
        count = dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")

def main():
    #print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_paths = [book_path for book_path in sys.argv if book_path != sys.argv[0]]
    #print(book_paths)
    for path in book_paths:
        book = get_book_text(path)
        word_count = get_word_count(book)
        char_freq_dict = char_occurrnce(book)
        sorted_list = dict_sort(char_freq_dict)
        output_bookbot(path, word_count, sorted_list)


main()