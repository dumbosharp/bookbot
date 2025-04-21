# gets the word count of a string
def word_count(book):
    words = book.split()
    word_count = len(words)
    return word_count

# gathers the amount of each type of character 
def char_count(book):
    char_dict = {}
    for char in book:
        char_lower = char.lower()
        if char_lower not in char_dict:
            char_dict[char_lower] = 1
        else:
            char_dict[char_lower] += 1
    return char_dict

# creates a list of dicts that only contain alphabetical chars and their count
def organize(dict):
    dict_list = []
    for char in dict:
        if char.isalpha():
            dict_list.append({"char": char, "num": dict[char]})
    return dict_list

# takes each dictionary in your list and returns the value associated with the "num" key
def sort_on(dict):
    return dict["num"]



