import sys
import re
from nparser import Parser

expression = sys.argv[1]

# TODO pep8 says that we should catch specific errors 
def calc_eval(equation):
    nsp = Parser()
    try:
        equation = re.sub('(?<=\d|\))(\()', '*(', equation)
        equation = equation.replace('π', 'PI')
        equation = equation.replace('e', 'E')
        equation = equation.replace('√', 'sqrt')
        result = nsp.eval(equation)
        return result
    except:
        return 'Unknown error occured.'


print(calc_eval(expression))
sys.stdout.flush()
