import random
import string

ALLOWED = string.ascii_letters + string.digits

def fix_punctuation(text):
    words = []
    current_word = ''
    for char in text:
        if char in ALLOWED:
            current_word += char
        else:
            if current_word:
                words.append(current_word)
                current_word = ''
            words.append(char)
    if current_word:
        words.append(current_word)
    return words

def disorder_words(words):
    disorder_text = []
    for word in words:
        if len(word) <= 3 or not any(char in ALLOWED for char in word[1:-1]):
            disorder_text.append(word)
        else:
            first_letter = word[0]
            last_letter = word[-1]
            middle_letters = list(word[1:-1])
            random.shuffle(middle_letters)
            disorder_word = first_letter + ''.join(middle_letters) + last_letter
            disorder_text.append(disorder_word)
    return ''.join(disorder_text)

