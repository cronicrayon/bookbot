#print("hello world")

def main():
    #gets all the variables needed for the print_report function
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_dict = character_count(text)
    #print(text)
    #print(f"{word_count} words")
    #print(character_dict)
    print_report(book_path, word_count, character_dict)
    

def get_word_count(text):
    # splits the text a list that counts all items to find word count
    words = text.split()
    return len(words)

def get_book_text(path):
    #uses the file path to load the wanted book and puts it in a string
    with open(path) as f:
        return f.read()

def character_count(text):
    #first takes string and changes all uppercase to lowercase
    uncased_text = text.lower()
    #second create empty dict then loops through uncased text adding 1 to the count of character 
    # if already in the dictionary or adding the character to it if it is not there
    character_dict = {}
    for character in uncased_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def print_sort_character_count(character_dict):
    #converts character dictionary to a list
    character_list = list(character_dict.items())
    #takes the character list and sorts it by the number of character Appearances in descending order
    sorted_characters = sorted(character_list, key=lambda item: item[1], reverse=True)
    #loops through the sorted list checks is it is from the alphabet and then prints the character and how many there are
    for character, count in sorted_characters:
        if character.isalpha():
            print(f"The '{character}' character was found {count} times")

def print_report(path, wordcount, character_dict):
    #takes all the report variables and prints them in one function
    print(f"--- Begin report of {path} ---")
    print(f"{wordcount} words found in the document")
    print_sort_character_count(character_dict)
    print("--- End report ---")


main()