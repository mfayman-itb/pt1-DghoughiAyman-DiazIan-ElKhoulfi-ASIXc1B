import random
import string

ALLOWED = string.ascii_letters + string.digits
blacklist = []
#region defs
def get_input():
    text = input('putin: ')
    words = text.split()
    return words

def fix_punctuation(words):
    punct = ""
    current_chunk = ""
    pos = ""
    result = []
    for word in words:
        for char in word:
            if char in ALLOWED:
                current_chunk += char
            elif char not in ALLOWED and (word.index(char) == 0 or word[:-1].index(char) == len(word) - 1):
                if word.index(char) == 0:
                    pos = 0
                else:
                    pos = 1
                punct = char
            else:
                #blacklist.append(char)
                current_chunk += char
        if pos == 0:
            result.append(punct)
            result.append(current_chunk)
        else:
            result.append(current_chunk)
            result.append(punct)
    print(result)
    return result



def disorder_words(result):
    disorder_text = []
    for word in result:
        #for punct in blacklist:
        if len(word) <= 3:
            disorder_text.append(word)
            continue
        first_letter = word[0]
        last_letter = word[-1]
        middle_letters = list(word[1:-1])  # Corregido aquí
        random.shuffle(middle_letters)
        disorder_word = first_letter + ''.join(middle_letters) + last_letter
        disorder_text.append(disorder_word)
    return ' '.join(disorder_text)

def main():
    text = get_input()
    result = fix_punctuation(text)
    print(disorder_words(result))
#endregion

main()
