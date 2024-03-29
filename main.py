def get_book(filepath):
  with open(filepath) as f:
    return f.read()

def get_word_count(book):
  return len(book.split())

def main():
  path = "books/frankenstein.txt"
  book = get_book(path)
  word_count = get_word_count(book)

  print(f"This book has {word_count} words.")

main()