"""
Ayman Dghoughi, Ian Díaz i Nizar ElKhoulfi
20/03/2024
ASIXc1 UF2 A2 Disseny Modular i Descendent
Descripció: principal program to disorder strings
"""
#region Imports
from logger import *
import random
import string
#endregion

#region Variables and Constants
ALLOWED = string.ascii_letters
#endregion
allDisordered = []

#region Functions

def check_input(text):
    if not text or len(str(text)) <= 3:
        print("Text is empty or too short.")
        logger('error', 'Text is empty or too short.')
        exit(1)
    else:
        logger('info', 'Input validated succesfully.')
        return str(text)


def fix_punctuation(text):
    try:
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
    except Exception as e:
        print(e)
        logger('error', e)
    logger('info', 'Punctuation fixed succesfully.')
    return words

def disorder_words(words):
    try:
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
    except Exception as e:
        print(e)
        logger('error', e)
    logger('info', 'Words disordered succesfully.')
    return ''.join(disorder_text)
#endregion
