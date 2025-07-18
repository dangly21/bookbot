import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import num_words
from stats import num_chars 
from stats import sort_list

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    text = get_book_text(sys.argv[1])
    num = num_words(text)
    char_dict = num_chars(text)
    my_list = sort_list(char_dict)
    print (f"Found {num} total words")
    print("---------- Character Count -------")
    for items in my_list:
        char = items["char"]
        count = items["num"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()
    

    