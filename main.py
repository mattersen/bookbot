def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count_dict = count_chars(text)
    print(text)
    print(f"There are {word_count} words in this book.")
    print(char_count_dict)

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

main()