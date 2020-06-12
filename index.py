
from input_module import getInput
from output_module import showOutput
from process_module import process

while True:
    inp = getInput()
    result = process(inp)
    showOutput(result)