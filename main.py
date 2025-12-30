from stats import get_num_words
from stats import get_chars
from stats import chars_dict_to_sorted_list
import sys

def main():
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = get_chars(text)
    charlist = chars_dict_to_sorted_list(chars)
    print(f"Found {num_words} total words")
    
    for e in charlist:
        if e["char"].isalpha():
            print(f"{e['char']}: {e['num']}")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
