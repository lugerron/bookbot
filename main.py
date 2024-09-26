def main():
    num_words = 0
    dictionary = {}
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    dictionary = count_characters(file_contents)

    print_report(num_words, dictionary, "books/frankenstein.txt")

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_dictionary = {}
    words = text.split()

    for word in words:
        lowered_word = word.lower()
        for char in lowered_word:
            if char not in char_dictionary and char.isalpha():
                char_dictionary[char] = 1
            elif char.isalpha():
                char_dictionary[char] += 1
    #TODO: Convert your dictionary of characters into a list of dictionaries and then use the .sort() method to sort by the number of occurrences.
    return char_dictionary

def dict_to_list(dict_to_convert):
    dict_list = []
    for value in dict_to_convert:
        tmp_dict = {}
        tmp_dict["name"] = value
        tmp_dict["num"] = dict_to_convert[value]
        dict_list.append(tmp_dict)
    return dict_list

def sort_on(dict_to_sort):
    return dict_to_sort["num"]

def print_report(word_count, word_dict, book_name):
    list_to_print = dict_to_list(word_dict)
    list_to_print.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_name} ---")
    print(f"{word_count} words found in the document.")
    print("")
    
    for list_dict in list_to_print:
        print(f"The '{list_dict['name']}' character was found {list_dict['num']} times.")
    print("--- End report ---")
    return None

main()