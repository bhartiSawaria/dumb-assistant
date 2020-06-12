
from input_module import getInput
from output_module import showOutput
from process_module import process
from welcome import getGreetingMessage

showOutput(getGreetingMessage())

while True:
    inp = getInput()
    result = process(inp)
    showOutput(result)