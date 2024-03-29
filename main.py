def get_book(filepath):
  with open(filepath) as f:
    return f.read()

def get_words(book):
  return book.split()

def get_word_count(book):
  return len(get_words(book))

# given a word list
# for each word, split up the word into letters
# for each letter, add it to the dictionary (if not there), or increment it
def get_char_count(book):
  char_count = {}
  word_list = get_words(book)

  for word in word_list:
    for char in word.lower():
      if char in char_count:
        char_count[char] += 1
      else:
        char_count[char] = 1

  return char_count

def main():
  path = "books/frankenstein.txt"
  book = get_book(path)
  word_count = get_word_count(book)

  print(f"This book has {word_count} words.")

  char_count = get_char_count(book)

  print(char_count)

main()