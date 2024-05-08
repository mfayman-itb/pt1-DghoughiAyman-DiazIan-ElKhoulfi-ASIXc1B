"""
Ayman Dghoughi, Ian Díaz i Nizar ElKhoulfi
08/05/2024
ASIXc1 UF2 A2 Disseny Modular i Descendent
Descripció: Release 3 Paraules boges
"""
#region Imports
from data_source import *
from crazy_words import *
from logger import *
import signal
import time
#endregion
start = time.time()

#region Functions
def sigint(sig, frame):
    logger('info', f'Program ended due to SIGINT, done in {timeElapsed():.3f}')
    exit(2)
def timeElapsed():
    end = time.time()
    lapse = end-start
    return lapse
signal.signal(signal.SIGINT, sigint)
def main():
    get_data_from_directory()
    for i in range(len(allText)):
        text = check_input(allText[i])
        logger('info', f'Input validated ({filenames[i]})')
        text = fix_punctuation(text)
        logger('info', f'Punctuation fixed ({filenames[i]})')
        allDisordered.append(disorder_words(text))
        logger('info', f'Text disordered ({filenames[i]})')
    write_data_to_files()

#endregion

#region main

try:
    logger('info', 'Program started, loading input data.')
    main()
except Exception as e:
    logger('error', f'{e}')
finally:
    logger('info', f'Program ended, time elapsed: {timeElapsed():.3f}')
#endregion

