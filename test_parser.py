import re
from nparser import Parser
import time


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


if __name__ == '__main__':
    start = time.time()
    eq = 'sin(π)'
    print(f'Calculating {eq}')
    calc_eval(eq)
    print(f'Took {time.time()-start}')
    print()

    start = time.time()
    eq = '√(9)'
    print(f'Calculating {eq}')
    print(calc_eval(eq))
    print(f'Took {time.time()-start}')
    print()

    start = time.time()
    eq = 'e'
    print(f'Calculating {eq}')
    calc_eval(eq)
    print(f'Took {time.time()-start}')
    print()
    
    start = time.time()
    eq = 'e^1'
    print(f'Calculating {eq}')
    calc_eval(eq)
    print(f'Took {time.time()-start}')
