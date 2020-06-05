import sys
import re
from nparser import Parser

expression = sys.argv[1]


def calc_eval(equation):
    nsp = Parser()
    try:
        equation = re.sub('(?<=\d|\))(\()', '*(', equation)
        equation = equation.replace('π', 'PI')
        equation = equation.replace('e', 'E')
        result = nsp.eval(equation)
        return result
    except:
        return 'Unknown error occured.'


print(calc_eval(expression))
sys.stdout.flush()
