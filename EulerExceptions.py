# Base class for all custom exceptions
class CalculatorException(Exception):
    pass


class InputError(CalculatorException):
    def __init__(self, input_expression, message):
        self.input_expression = input_expression
        self.message = message
