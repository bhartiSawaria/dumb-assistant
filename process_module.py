
from output_module import showOutput
from input_module import getInput
from database import getResultFromDatabase
from time_modules import *

def process(query):
    answer = getResultFromDatabase(query)
    if answer == 'getTime':
        return getTime()

    elif answer == 'getDate':
        return getDate()


