import random

#region defs
def file_input():
    text = input('putin: ')
    return text

"""
def verify_file():

def contains_text():
"""
def disorder_words(text):
    words = text.split()
    disorder_text = []
    for word in words:
        if len(word) <= 3:
            disorder_text.append(word)
            continue
        first_word = word[0]
        last_word = word[-1]
        middle_letters = list(word[1:-1])  # Corregido aquí
        random.shuffle(middle_letters)
        disorder_word = first_word + ''.join(middle_letters) + last_word
        disorder_text.append(disorder_word)
    return ' '.join(disorder_text)

#endregion

text = file_input()
print(disorder_words(text))
