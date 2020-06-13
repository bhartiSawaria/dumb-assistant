
from input_module import getInput
from output_module import showOutput
from process_module import process
from welcome import getGreetingMessage
import os
os.system('cls')


showOutput(getGreetingMessage())

while True:
    inp = getInput()
    result = process(inp)
    showOutput(result)