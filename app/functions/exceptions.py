# Base class for all custom exceptions
class CalculationError(Exception):
    pass


class InputError(CalculationError):

    def __init__(self, input_expression,  message):
        self.input_expression = input_expression
        self.message = message
