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

def sort_num(d):
    for key, value in d.items():
        return value


def print_report():
    word_count_dict = count_char()
    list_of_words = []

    # Loop through dictionary
    for key, value in word_count_dict.items():
        if key.isalpha():
            list_of_words.append({key:value})


    list_of_words.sort(reverse=True, key=sort_num)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(book_path)} words found in the document")
    # Loop through list which contains dictionaries
    for word in list_of_words:
        for key, value in word.items():
            print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def main():
    print_report()

main()

