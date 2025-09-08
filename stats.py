def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def char_count(book_text):
    characters = {}
    for char in book_text:
        if char.isalpha():
            char = char.lower()
            if char not in characters:
                characters[char] = 0
            characters[char] += 1
    characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    return characters
