import sys
import re
from parse import Parser
import functions.output_display as display


def evaluate(expression: str, is_rad: bool, is_binary_output: bool, is_binary_input: bool) -> str:
    """Evaluates a mathematical expression passed as a string and returns the result as another string.

    Args:
        expression (str): Expression to evaluate
        is_rad (str): Determines if in radian mode
        is_binary (str): Determines if the output should be binary or not
        is_binary_input (str): Determines if the input should be binary or not

    Returns:
        str: Result of evaluation of expression
    """

    if exp_is_blank(expression):
        return ""

    parser = Parser(is_rad, is_binary_input)
    try:
        # Make implicit multiplications between bracketed items explicit.
        expression = re.sub('(?<=\d|\))(\()', '*(', expression)
        # Ensure that characters used can be read by parser.
        # Map euler's constant to the letter e when not surrounded by other letters
        expression = re.sub('(?![a-zA-Z])e(?![a-zA-Z])', 'E', expression)
        expression = expression.replace('π', 'PI')
        expression = expression.replace('√', 'sqrt')

        # Evaluate expression
        evaluation = parser.evaluate(expression)
        if is_binary_output:
            evaluation = display.decimal_to_binary(evaluation)
        return evaluation
    except Exception as e:
        return str(e)


def exp_is_only_num(expression: str) -> bool:
    """Evaluates mathematical expression passed to determine if it is a number (float or int)

    Args:
        expression (str): Expression to evaluate

    Returns:
        bool: Result of evaluation of expression type
    """
    try:
        float(expression)
        return True
    except ValueError:
        return False


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
    is_rad = sys.argv[2].lower() == "true"
    is_binary_output = sys.argv[3].lower() == "true"
    is_binary_input = sys.argv[4].lower() == "true"
    print(evaluate(expression, is_rad, is_binary_output, is_binary_input))
