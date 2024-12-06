book_path = "./books/frankenstein.txt"

def book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    count_book = book_text(book)
    return len(count_book.split())

def count_char():
    book_dict = dict()
    book_list = book_text(book_path).split()
    book_string = ''.join(book_list).lower()

    # Loop through book_string
    for char in book_string:
        if char in book_dict:
            book_dict[char] += 1
        else:
            book_dict[char] = 1

    return book_dict

def main():
    count_char()

main()

