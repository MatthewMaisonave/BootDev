def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    #print(file_contents)
    return file_contents

def get_word_count(text):
    word_list = text.split()
    num_words = len(word_list)
    print(f"Found {num_words} total words")
    return num_words

def main():
    path = "books/frankenstein.txt"
    book = get_book_text(path)
    word_count = get_word_count(book)


main()