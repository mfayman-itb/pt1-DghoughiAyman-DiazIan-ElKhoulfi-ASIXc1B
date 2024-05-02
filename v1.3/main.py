"""
Ayman Dghoughi, Ian Díaz i Nizar ElKhoulfi
20/03/2024
ASIXc1 UF2 A2 Disseny Modular i Descendent
Descripció: main program and menu
"""
#region Imports
from data_source import *
from crazy_words import *
from logger import *
from SystemColors import *
import signal
import time
#endregion
start = time.time()
def sigint(sig, frame):
    end = time.time()
    lapse = end-start
    logger('info', 'Program ended due to SIGINT, done in %3.f', lapse)
    exit(2)

signal.signal(signal.SIGINT, sigint)
def main():
    text = get_data_from_file()
    check_input(text)
    text = fix_punctuation(text)
    text = disorder_words(text)
    write_data_to_file(text)
#region Functions

#endregion

#region main

main()
#endregion

