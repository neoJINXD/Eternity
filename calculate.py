import sys
import re
from parse import Parser
import functions.output_display as display


def evaluate(expression: str, is_rad:bool) -> str:
    """Evaluates a mathematical expression passed as a string and returns the result as another string.

    Args:
        expression (str): Expression to evaluate
        is_rad (bool): Determines if in radian mode

    Returns:
        str: Result of evaluation of 'expression
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


        #Convert numbers directly to rad
        if input_is_only_num(expression):
            if is_rad == "true":
                expression = "2"
            elif is_rad == "false":
                expression = "1"

        # Evaluate expression
        return parser.evaluate(expression)
    except Exception as e:
        return str(e)

def input_is_only_num(expression):
    try:
        float(expression)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    expression = sys.argv[1]
    is_rad = sys.argv[2]
    print(evaluate(expression, is_rad.lower()))
