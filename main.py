from stats import word_count
from stats import letter_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    x = get_book_text("books/frankenstein.txt")
    print(f"{word_count(x)} words found in the document")
    print(letter_count(x))



main()
