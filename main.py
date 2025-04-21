import sys
import os
from stats import word_count
from stats import char_count
from stats import organize
from stats import sort_on

# puts all of a .txt file into a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

# tells you the word count and character count of a book
def main():
    
    # taking argument from command line and attaching it to filepath variable
    args = sys.argv
    if len(args) != 2:
            print("Usage: python3 main.py <path_to_book>")
            print("Only enter filepath to Book")
            sys.exit(1)
        
    filepath = args[1]

    # BEGINNING OF ERROR HANDLING

    # Check if file exists
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist")
        sys.exit(1)

    # Check if path is actually a file (not a directory)
    if not os.path.isfile(filepath):
        print(f"Error: '{filepath}' is not a file")
        sys.exit(1)

    # Check if file is readable
    if not os.access(filepath, os.R_OK):
        print(f"Error: Cannot read file '{filepath}' (permission denied)")
        sys.exit(1)

    # Check if file is empty
    if os.path.getsize(filepath) == 0:
        print(f"Error: File '{filepath}' is empty")
        sys.exit(1)
    
    # check if file is binary/corrupt/some odd encoder
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            contents = f.read()
    except UnicodeDecodeError:
        print(f"Error: File '{filepath}' is not a valid text file or has an unsupported encoding")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

        # END OF ERROR HANDLING

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
