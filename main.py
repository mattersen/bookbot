def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    print(text)
    print(count)


def get_book_text(path):    
    with open(path) as f:
        return f.read()
    
def count_words(string):
    words = string.split()
    count = len(words)
    return count

main()