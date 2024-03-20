#region Imports
from data_source import *
from crazy_words import *
import random
import string
#endregion

#region Variables i constants
#endregion

#region Funcions
def menu():
    try:
        options = ['1','2','3','4']
        print(f"1:\tGet the data from the keyboard.\n2:\tGet the data from an URL.\n3:\tGet the data from the answer to a ChatGPT prompt.\n4:\tGet the data from a file.")
        inp = input("Select option: ")
        while str(inp) not in options:
            print(f'Option "{inp}" not available.')
            print(f"1:\tGet the data from the keyboard.\n2:\tGet the data from an URL.\n3:\tGet the data from the answer to a ChatGPT prompt.\n4:\tGet the data from a file.")
            inp = int(input("Select option: "))
        match inp:
            case '1': text = get_input(inp)
            case '2': text = get_data_from_server(inp)
            case '3':
                apikey = get_gpt_api_key(inp)
                text = get_data_from_chatgpt(apikey, inp)
            case '4': text = get_data_from_file(inp)
        return text
    except Exception as e:
        print(e)

def main():
    text = menu()
    clean = fix_punctuation(text)
    result = disorder_words(clean)
    return print(result)
#endregion

#region main
main()
#endregion
