import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import num_of_words
from stats import count_characters
from stats import report

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    book_text = get_book_text(sys.argv[1])
    word_count = num_of_words(book_text)
    char_count = count_characters(book_text)
    sorted_chars  = report(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for sort in sorted_chars:
        char = sort["char"]
        count = sort["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()