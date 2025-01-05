
def count_word_in_book(content):
  words = content.split()

  count = 0

  for word in words:
    count += 1

  return count

def character_count(content):
    character_count_dict = {}
    
    for character in content.lower():
        if character.isalpha():  
            character_count_dict[character] = character_count_dict.get(character, 0) + 1
    
    return character_count_dict



  

def main():
  book_path = "books/frankenstein.txt"
  try:
    book_content = ""
    with open(book_path) as f:
      book_content = f.read()
    
    word_count = count_word_in_book(book_content)

    character_count_dict = character_count(book_content)

    sorted_dict = dict(sorted(character_count_dict.items(), key=lambda x: x[1], reverse=True))    

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for key, value in sorted_dict.items():
      print(f"The \'{key}\' character was found {value} times\n")
    
    print(f"--- End report ---")

  
main()