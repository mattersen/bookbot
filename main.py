def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count_dict = count_chars(text)
    unique_chars_list = dict_to_list(char_count_dict)
    unique_chars_list.sort(reverse=True, key=sort_on)
    alpha_only_dict = alpha_dict(unique_chars_list)

    print_report(alpha_only_dict, book_path, word_count)

def get_book_text(path):    
    with open(path) as f:
        return f.read()

def count_chars(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1 
    return char_dict

def count_words(text):
    words = text.split()
    count = len(words)
    return count

def dict_to_list(dict):
    list = []
    for char in dict:
        list.append({"char" : char, "num": dict[char]})
    return list

def alpha_dict(list_of_dict):
    alpha_dict = {}
    for dict in list_of_dict:
        if dict["char"].isalpha():
            alpha_dict[dict["char"]] = dict["num"]
    return alpha_dict

def sort_on(dict):
    return dict["num"]

def print_report(alpha_sorted_dictionary: dict[str, int], book_path: str, word_count: int):
    print(f"--- Begin report of {book_path} ---")
    print(f"There are {word_count} words in this book.")
    print("")
    for char, num in alpha_sorted_dictionary.items():
        print(f"The '{char}' character was found {num} times")
    print("--- End Report ---")

main()