from stats import word_count
from stats import char_count
from stats import organize
from stats import sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    filepath = "books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    whole_book = get_book_text(filepath)
    words = word_count(whole_book)
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    letters = char_count(whole_book)
    letters_organized = organize(letters)
    letters_organized.sort(reverse = True, key = sort_on)
    for dict in letters_organized:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")



main()
