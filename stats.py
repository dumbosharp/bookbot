
def word_count(book):
    words = book.split()
    word_count = len(words)
    return word_count

def letter_count(book):
    char_dict = {}
    for char in book:
        char_lower = char.lower()
        if char_lower not in char_dict:
            char_dict[char_lower] = 1
        else:
            char_dict[char_lower] += 1
    return char_dict



