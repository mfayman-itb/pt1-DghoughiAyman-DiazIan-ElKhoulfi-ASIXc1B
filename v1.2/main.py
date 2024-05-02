"""
Ayman Dghoughi, Ian Díaz i Nizar ElKhoulfi
20/03/2024
ASIXc1 UF2 A2 Disseny Modular i Descendent
Descripció: main program and menu
"""
#region Imports
from data_source import *
from crazy_words import *
import random
import string
#endregion

#region Functions
def menu():
    try:
        options = ['1','2','3','4']
        print(f"\n1:\tGet the data from the keyboard.\n2:\tGet the data from an URL.\n3:\tGet the data from the answer to a ChatGPT prompt.\n4:\tGet the data from a file.\n")
        inp = input("Select option: ")
        while str(inp) not in options:
            print(f'Option "{inp}" not available.')
            print(f"\n1:\tGet the data from the keyboard.\n2:\tGet the data from an URL.\n3:\tGet the data from the answer to a ChatGPT prompt.\n4:\tGet the data from a file.\n")
            inp = input("Select option: ")
        match inp:
            case '1': text = get_input(inp)
            case '2': text = get_data_from_server()
            case '3':
                apikey = get_gpt_api_key()
                text = get_data_from_chatgpt(inp)
            case '4': text = get_data_from_file(inp)
        return text, inp
    except Exception as e:
        print(e)
#endregion

#region main
def main():
    text, option = menu()
    text = check_input(text, option)
    clean = fix_punctuation(text)
    result = disorder_words(clean)
    return print(result)

main()
#endregion

