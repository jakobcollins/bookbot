def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main(filepath):
    book_text = get_book_text(filepath)
    return book_text

def word_count(filepath):
    book_text = get_book_text(filepath)
    words = book_text.split()
    print(f"{len(words)} words found in the document")


word_count("books/frankenstein.txt")