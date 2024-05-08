"""
Ayman Dghoughi, Ian Díaz i Nizar ElKhoulfi
08/05/2024
ASIXc1 UF2 A2 Disseny Modular i Descendent
Descripció: Release 3 Paraules boges
"""
#region Imports
from logger import *
from crazy_words import *
import os
import requests
import json
from openai import OpenAI
#endregion

inputDir = os.path.join('.','entrada')
outputDir = os.path.join('.','sortida')
allText = []
filenames = []

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

def get_data_from_directory():
    for root, dirs, files in os.walk(inputDir):
        for file in files:
            if file.endswith('.txt'):
                with open(os.path.join(root, file), 'r') as txt:
                    text = txt.read()
                    allText.append(text)
                    filenames.append(file)
    logger('info', f'All input data loaded ({filenames})')

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

def write_data_to_files():
    if not os.path.exists(outputDir):
        os.mkdir(os.path.join('.', 'sortida'))
    for i in range(len(filenames)):
        filenames[i] = filenames[i].replace('.txt', '_boges.txt')
        disordered = allDisordered[i]
        with open(os.path.join(outputDir, filenames[i]), 'w') as outFile:
            outFile.write(disordered)

#endregion
