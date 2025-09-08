from stats import get_num_words, char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)  #extracts book text using get_book_text function
    num_words = get_num_words(book_text)    #counts words using get_num_words function // from the stats.py file
    chars = char_count(book_text)  #counts characters using char_count function // from the stats.py file

    print(f"""============ BOOKBOT ============
Analyzing book found at {filepath}...
----------- Word Count ----------""")
    print(f"Found {num_words} total words")
    print("-------- Character Count -------")
    for char in chars:
        print(f"{char}: {chars[char]}")

main()