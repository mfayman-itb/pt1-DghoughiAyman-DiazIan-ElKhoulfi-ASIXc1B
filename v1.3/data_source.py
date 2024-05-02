"""
Ayman Dghoughi, Ian Díaz i Nizar ElKhoulfi
20/03/2024
ASIXc1 UF2 A2 Disseny Modular i Descendent
Descripció: definitions of different types of inputs (text, url, chatgpt and file)
"""
#region Importsç
from logger import *
import os
import requests
import json
from openai import OpenAI
#endregion


#region Functions
def get_data_from_file():
    file = os.path.join('.', 'paraules.txt')
    if os.path.exists(file):
        with open(file, 'r') as file:
            text = file.read()
    else:
        print(f'File "{file}" not found.')
        logger('error', f'File {file} not found.')
        exit(1)
    logger('info', 'Succesfully loaded the data.')
    return text

def write_data_to_file(text):
    try:
        file = os.path.join('.', 'paraules_boges.txt')
        if os.path.exists(file):
            with open(file, 'wt') as file:
                file.write(text)
        else:
            logger('error', f'File not found: {file}')
    except Exception as e:
        logger('error', e)
    logger('info', f'Results saved to: {file}')
#endregion

