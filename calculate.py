import sys
import re

expression = sys.argv[1]


def calcEval(equation):
    """
    calcEval() uses eval(), which is normally a dangerous thing to do.
    To combat this, a list of allowed inputs are made so eval() only
    gets called if the "equation" given contains only allowed inputs.
    """

    characters = list(equation)

    allowedInputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                     '+', '-', '*', '/', '^', ' ', '(', ')', '.', 'cos', 'sin']

    checkSet = set(characters + allowedInputs)

    if len(checkSet) != len(allowedInputs):
        return "Error: Unknown input character."

    else:
        try:
            equation = re.sub('(?<=\d|\))(\()', '*(', equation)
            equation = equation.replace('^', '**')
            return (eval(equation))
        except SyntaxError:
            return 'Unknown error occured.'


print(calcEval(expression))
sys.stdout.flush()
