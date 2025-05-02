def num_of_words(book_text):
    word_count = len(book_text.split())
    return word_count

def count_characters(book_text):
    lower_chars = book_text.lower()
    characters = {}
    for char in lower_chars:
        if char in characters:
            characters[char] +=1
        else:
            characters[char] = 1
    return characters

def report(char_count):
    chars_list = []
    for char, count in char_count.items():
        chars_list.append({"char": char, "num": count})
    def sort_on(dict):
        return dict["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list

