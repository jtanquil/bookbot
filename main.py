def get_book(filepath):
  with open(filepath) as f:
    return f.read()

def get_words(book):
  return book.split()

def get_word_count(book):
  return len(get_words(book))

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

# given a dictionary of character counts,
# convert the dictionary into a list of key/value pairs
# filter out the non-alphabetic characters
# sort by # of occurrences, in descending order
# print the dictionary
def print_char_count(char_count):
  def sort_by_count(char_dict):
    return char_dict["count"]

  char_list = [{"char": char, "count": char_count[char]} for char in char_count if char.isalpha()]
  char_list.sort(reverse = True, key = sort_by_count)

  for char_dict in char_list:
    print(f"The '{char_dict["char"]}' character was found {char_dict["count"]} times.")

def main():
  path = "books/frankenstein.txt"
  book = get_book(path)
  word_count = get_word_count(book)

  print(f"--- Begin report of {path} ---")
  print(f"This book has {word_count} words.")

  char_count = get_char_count(book)

  print_char_count(char_count)
  print("--- End report ---")

main()