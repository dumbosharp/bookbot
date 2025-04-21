
def word_count(book):
    words = book.split()
    word_count = len(words)
    return word_count

def char_count(book):
    char_dict = {}
    for char in book:
        char_lower = char.lower()
        if char_lower not in char_dict:
            char_dict[char_lower] = 1
        else:
            char_dict[char_lower] += 1
    return char_dict

def organize(dict):
    dict_list = []
    for char in dict:
        if char.isalpha():
            dict_list.append({"char": char, "num": dict[char]})
    return dict_list

def sort_on(dict):
    return dict["num"]



