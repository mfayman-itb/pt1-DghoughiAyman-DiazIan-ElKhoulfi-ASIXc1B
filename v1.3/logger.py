import os
import logging
from SystemColors import *

logFile = os.path.join('.', 'boges.log')
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

logger('info', 'funxiona')