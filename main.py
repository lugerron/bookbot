def main():
    num_words = 0
    dictionary = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    dictionary = count_characters(file_contents)

    print(num_words)
    print(dictionary)

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dictionary = {}
    words = text.split()

    for word in words:
        lowered_word = word.lower()
        for char in lowered_word:
            if char not in char_dictionary:
                char_dictionary[char] = 1
            else:
                char_dictionary[char] += 1
    
    return char_dictionary

main()