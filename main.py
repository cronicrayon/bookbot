#print("hello world")

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_list = character_count(text)
    print(text)
    print(f"{word_count} words")
    print(character_list)
    

def get_word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(text):
    uncased_text = text.lower()
    character_dict = {}
    for character in uncased_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict




main()