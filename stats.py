def word_count(book):
    words = book.split()
    word_count = len(words)
    return word_count

def letter_count(book):
    char_dict = {}
    for char in book:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    return char_dict



