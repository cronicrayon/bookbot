#print("hello world")

def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordlist = file_contents.split()
    print(file_contents)
    print("Word count " , len( wordlist))

main()