def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_counter(text)
    chars = char_counter(text)
    list = sorter(chars)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()
    for i in range(len(list)):
        print(f"The '{list[i]['letter']}' character was found {list[i]['times']} times")
    print(f"--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_counter(book_text):
    words = book_text.split()
    return len(words)


def char_counter(book_text):
    chars = {}
    lower_case = book_text.lower()
    char_list = list(lower_case)
    for char in char_list:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(dict):
    return dict["times"]

def sorter(char_dict):
    list_dict = []
    for char in char_dict:
        if char.isalpha() == True:
            list_dict.append({"letter":char, "times":char_dict[char]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

main()