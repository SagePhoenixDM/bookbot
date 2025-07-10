# %% importing other functions
from stats import get_num_words
from stats import get_num_chars
from stats import dict_split
import sys

# %% new functions


# get book contents
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


# %% main


def main():
    # checking if system arguments has more than one argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    
    # getting text
    book_contents = get_book_text(book_path)

    # processing text
    num_words = get_num_words(book_contents)
    num_chars = get_num_chars(book_contents)
    sort_dict = dict_split(num_chars)

    # printing output
    print("=" * 12, "BOOKBOT", "=" * 12)
    print(f"Analyzing book found at {book_path}")
    print("-" * 11, "Word Count", "-" * 10)
    print(f"Found {num_words} total words")
    print("-" * 9, "Character Count", "-" * 7)
    for i in range(len(sort_dict)):
        if sort_dict[i]["char"].isalpha():
            print(sort_dict[i]["char"] + ":", sort_dict[i]["num"])
    print("=" * 13, "END", "=" * 15)


# %% calling main


main()