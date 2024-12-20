def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"{count_words(file_contents)} words found in the document")
    for letter, count in count_unique_letters(file_contents).items():
        print(f"The '{letter}' character was found {count} times")

def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_unique_letters(file_contents):
    letters = {}
    for char in file_contents:
        char = char.lower()
        if char.isalpha():
            letters[char] = letters.get(char, 0) + 1
            
    return dict(sorted(letters.items()))

if __name__ == "__main__":
    main()