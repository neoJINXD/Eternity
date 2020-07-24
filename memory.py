import sys
import re
from parse import Parser

expression = sys.argv[1]
history = []


def record(equation):
    global history
    history.append(equation)
    return history


def clear():
    global history
    history = []
    return history


print(record(expression))
sys.stdout.flush()
