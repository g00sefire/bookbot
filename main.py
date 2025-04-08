from stats import get_num_words, count_repitions, sorted_dict
import sys

def main():
    print("============ BOOKBOT ============")
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(book_path)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    with open(book_path) as f:
        file_contents = f.read()
        char_counts = count_repitions(file_contents)
    sorted_count = sorted_dict(char_counts)
    b = 'a'.isalpha
    for pair in sorted_count:
        if (pair[0].isalpha()):
            print(f"{pair[0]}: {pair[1]}")
    print("============= END ===============")

if __name__ == '__main__':
     main()