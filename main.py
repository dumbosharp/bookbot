def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def word_count(book):
    words = book.split()
    word_count = len(words)
    return word_count


def main():
    x = get_book_text("books/frankenstein.txt")
    print(f"{word_count(x)} words found in the document")


main()
