def get_word_count(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def char_occurrnce(text):
    char_dict = {}
    char_list = list(text.lower())
    for char in char_list:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict 

def sort_on(char_dict):
    return char_dict["num"]

def dict_sort(char_dict):
    sorted_list = []
    for char in char_dict:
        count = char_dict[char]
        new_dict = {"char": char, "num": count}
        sorted_list.append(new_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list