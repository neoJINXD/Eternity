import sys
import re
from parse import Parser


def evaluate(expression: str) -> str:
    """Evaluates a mathematical expression passed as a string and returns the result as another string.

    Args:
        expression (str): Expression to evaluate

    Returns:
        str: Result of evaluation of 'expression'
    """
    parser = Parser()
    try:
        # Make implicit multiplications between bracketed items explicit.
        expression = re.sub('(?<=\d|\))(\()', '*(', expression)
        # Ensure that characters used can be read by parser.
        # Math euler's constant to the letter e when not surrounded by other letters
        expression = re.sub('(?![a-zA-Z])e(?![a-zA-Z])', 'E', expression)
        expression = expression.replace('π', 'PI')
        expression = expression.replace('√', 'sqrt')
        # Evaluate expression
        return parser.evaluate(expression)
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    expression = sys.argv[1]
    print(evaluate(expression))
