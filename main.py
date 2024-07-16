def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count_dict = count_characters(text)
    character_count_list = list(character_count_dict.items())
    sorted_list = sorted(character_count_list, key=sort_on, reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for el in sorted_list:
        if el[0].isalpha() == True:
            print(f"The '{el[0]}' was found {el[1]} times")
    print("--- End Report ---")

def sort_on(list):
    return list[1]


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in character_dict:
            character_dict[lowered] += 1
        else:
            character_dict[lowered] = 1
    return character_dict

main()
    
