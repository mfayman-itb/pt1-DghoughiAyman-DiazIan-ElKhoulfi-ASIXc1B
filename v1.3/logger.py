"""
Ayman Dghoughi, Ian Díaz i Nizar ElKhoulfi
08/05/2024
ASIXc1 UF2 A2 Disseny Modular i Descendent
Descripció: Release 3 Paraules boges
"""

import os
import logging

logFile = os.path.join(os.path.join('.', 'log'), 'boges.log')
logFormat = '%(asctime)s - %(levelname)s - %(message)s'
logLevel = logging.DEBUG
logMode = 'at'
color_code = 0
logging.basicConfig(level=logLevel, format=logFormat, filename=logFile, filemode=logMode)
def logger(type, message):
    match type:
        case 'error': logging.error(message)
        case 'info': logging.info(message)
        case 'warning': logging.warning(message)
        case 'debug': logging.debug(message)
        case 'critical': logging.critical(message)
