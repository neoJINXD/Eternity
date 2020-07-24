import sys
import re
from parse import Parser
import functions.output_display as display


def evaluate(expression: str, is_rad: str, is_binary: str) -> str:
    """Evaluates a mathematical expression passed as a string and returns the result as another string.

    Args:
        expression (str): Expression to evaluate
        is_rad (str): Determines if in radian mode
        is_binary (str): Determines if the input and output is in binary

    Returns:
        str: Result of evaluation of expression
    """

    if exp_is_blank(expression):
        return ""

    parser = Parser(is_rad == "true", is_binary)
    try:
        # Make implicit multiplications between bracketed items explicit.
        expression = re.sub('(?<=\d|\))(\()', '*(', expression)
        # Ensure that characters used can be read by parser.
        # Math euler's constant to the letter e when not surrounded by other letters
        expression = re.sub('(?![a-zA-Z])e(?![a-zA-Z])', 'E', expression)
        expression = expression.replace('π', 'PI')
        expression = expression.replace('√', 'sqrt')


        # Evaluate expression
        evaluation = parser.evaluate(expression, is_binary)
        if is_binary == "true":
            evaluation = display.convert_to_binary(evaluation)
        return evaluation
    except Exception as e:
        return str(e)


def exp_is_blank(expression: str) -> bool:
    """Evaluates mathematical expression passed to determine if it is empty

        Args:
            expression (str): Expression to evaluate

        Returns:
            bool: Result of evaluation of expression length
        """
    return not (expression and expression.strip())


if __name__ == "__main__":
    # print(sys.argv)
    expression = sys.argv[1]
    is_rad = sys.argv[2]
    is_binary = sys.argv[3]
    print(evaluate(expression, is_rad.lower(), is_binary.lower()))

