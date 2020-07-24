from functions import common
from functions import exponents_and_logs
from functions import statistic
from functions import trigonometry
import functions.output_display as display
import exceptions.exceptions as exceptions

from pyparsing import (
    Literal,
    Word,
    Group,
    Forward,
    alphas,
    Regex,
    ParseException,
    CaselessKeyword,
    Suppress,
    delimitedList,
)


class Parser(object):
    """A class used to parse mathematical expressions.

    Methods:
        evaluate(expression, expected=None, parse_all=True)
            Returns the result of an expression in string form.
    """
    _symbol_stack = []

    def push_first(self: object, tokens: list) -> None:
        """Push first element of 'tokens' onto symbol stack.

        Used properly during parsing, this function can turn infix notation into postfix notation.

        Args:
            tokens (list): Tokens from which first token must be taken.
        """
        self._symbol_stack.append(tokens[0])

    def push_unary_operator(self: object, tokens: list) -> None:
        """Processes unary operators applied to atom and appends appropriate operators to symbol stack.

        For now, we have only two possible unary operators ('-' and '+').
        '+' does nothing and '-' turns the atom negative in odd numbers.

        Args:
            tokens (list): Tokens belonging to atom. Unary operators to apply to atom will be at start of list.
        """
        # We will track parity of unary '-'s to push the 'unary -' symbol onto the stack only once per atom and improve runtime.
        is_negative = False
        for e in tokens:
            if e == '-':
                is_negative = not is_negative
            elif e == '+':
                continue
            # The first symbol found that is not a unary operator marks the end of the unary operators.
            else:
                break
        if is_negative:
            self._symbol_stack.append('unary -')

    def __init__(self: object, is_rad: bool, is_binary: bool) -> None:
        """Define grammar to be used by parser and parse actions to be used in constructing the symbol stack.

        Args:
            is_rad (bool): Angle mode
            is_binary (bool): Binary input option
        """

        # Settings
        self._is_rad = is_rad
        self._is_binary = is_binary

        # Expressions
        expr = Forward()

        # Operations
        plus, minus, multiply, divide, mod = map(Literal, "+-*/%")
        left_bracket, right_bracket = map(Suppress, "()")
        addition_operation = plus | minus
        multiplication_operation = multiply | divide | mod
        power_operation = Literal("^")
        factorial_operation = Literal("!")

        # Functions
        def add_arg_count_to_tokens(tokens):
            function_id = tokens.pop(0)
            arg_count = len(tokens[0])
            tokens.insert(0, (function_id, arg_count))

        function_id = Word(alphas)
        # Expressions must be in groups so that we can count them separately.
        argument_list = delimitedList(Group(expr))
        function = (function_id + left_bracket + Group(argument_list) + right_bracket
                    ).setParseAction(add_arg_count_to_tokens)

        # Values
        e = CaselessKeyword("E")
        pi = CaselessKeyword("PI")
        number = Regex(r"[+-]?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?")
        value = (e | pi | number)

        # Expression grammars. Order of operations is determined here.
        factor = Forward()
        atom = (addition_operation[...] + (
                (function | value).setParseAction(self.push_first) |
                Group(left_bracket + expr + right_bracket)
        )).setParseAction(self.push_unary_operator)
        factor << atom + (
                (power_operation + factor) |
                factorial_operation
        ).setParseAction(self.push_first)[...]
        term = factor + (
                multiplication_operation + factor
        ).setParseAction(self.push_first)[...]
        expr << term + (
                addition_operation + term
        ).setParseAction(self.push_first)[...]
        self.bnf = expr

        # Mapping between constant names and providers
        self.constant_map = {"PI": trigonometry.generate_pi,
                             "E": exponents_and_logs.pow_e(1),
                             }
        # Mapping between operators and appropriate function calls
        self.operation_map = {"+": lambda a, b: a + b,
                              "-": lambda a, b: a - b,
                              "*": lambda a, b: a * b,
                              "/": lambda a, b: a / b,
                              "%": lambda a, b: a % b,
                              "^": exponents_and_logs.pow,
                              "!": common.factorial
                              }
        # Mapping between function ids and appropriate function calls.
        # Remember that function names must only contain letters.
        self.function_map = {
            # Exponential and logarithmic functions
            "sqrt": lambda a: exponents_and_logs.radical(a, 2),
            "radical": exponents_and_logs.radical,
            "root": exponents_and_logs.radical,
            "pow": exponents_and_logs.pow,
            "powTen": exponents_and_logs.pow_10,
            "powPi": exponents_and_logs.pow_pi,
            "powE": exponents_and_logs.pow_e,
            "exp": exponents_and_logs.pow_e,
            "ln": exponents_and_logs.ln,
            "log": exponents_and_logs.log,
            # Statistics functions
            "mean": statistic.mean,
            "mad": statistic.mad,
            "std": statistic.std
        }

        # Mapping between trig function ids and appropriate function calls.
        # Remember that function names must only contain letters.
        self.trig_map = {
            # Basic trigonometry functions
            "sin": trigonometry.sin,
            "cos": trigonometry.cos,
            "tan": trigonometry.tan,
            # Hyperbolic trigonometry functions
            "sinh": trigonometry.sinh,
            "cosh": trigonometry.cosh,
            "tanh": trigonometry.tanh,
        }

    def evaluate_stack(self: object, symbol_stack: list) -> str:
        """Return result of expression represented by postfix stack of symbols.

        Args:
            symbol_stack (list): Postfix stack of mathematical symbols.

        Returns:
            str: Result of expression
        """
        # Get current symbol.
        symbol = symbol_stack.pop()
        
        # If symbol is tuple, symbol is a function. Get function identifier and argument count.
        if isinstance(symbol, tuple):
            symbol, num_args = symbol

        # Process unary '-'
        if symbol == 'unary -':
            return -self.evaluate_stack(symbol_stack)
        # Process other unary operators
        if symbol == "!":
            operand = self.evaluate_stack(symbol_stack)
            return self.operation_map[symbol](operand)
        # Process binary operators
        operation = self.operation_map.get(symbol, False)
        if operation:
            operand_2 = self.evaluate_stack(symbol_stack)
            operand_1 = self.evaluate_stack(symbol_stack)
            return operation(operand_1, operand_2)
        # Process function calls
        operation = self.function_map.get(symbol, False)
        if operation:
            # Begin by getting arguments.
            # Note that arguments are pushed onto tack in reverse order.
            args = reversed([self.evaluate_stack(symbol_stack)
                             for _ in range(num_args)])
            return operation(*args)
        # Process trig function calls
        operation = self.trig_map.get(symbol, False)
        if operation:
            # Begin by getting arguments.
            # Note that arguments are pushed onto tack in reverse order.
            args = reversed([self.evaluate_stack(symbol_stack)
                             for _ in range(num_args)])
            return trigonometry.process_angle_mode(*args, self._is_rad, operation)
        # Process constants.
        operation = self.constant_map.get(symbol, False)
        if operation:
            return operation()
        # If symbol is not an operation or a constant, the symbol must be a numeral. Try casting to an int.
        try:
            value = int(symbol)
            if self._is_binary:
                value = display.binary_to_decimal_integer(value)
            return value
        except ValueError:
            pass
        # Try casting to a float.
        try:
            value = float(symbol)
            if self._is_binary:
                value = display.binary_to_decimal(value)
            return value
        except ValueError:
            pass
        # If none of the casts worked, we have some unrecognized symbol. Raise an exception.
        raise Exception("{0} is not a recognized symbol.".format(symbol))

    def evaluate(self: object, expression: str) -> float:
        """Return result of expression passed as string.

        Args:
            expression (str): Expression to evaluate.

        Returns:
            str: Result of expression
        """
        # Reset parser state
        self._symbol_stack = []

        # Try to evaluate expression.
        try:
            # Make postfix notation of infix notation.
            _ = self.bnf.parseString(expression, True)
            # Evaluate generated stack of postfix symbols.
            return self.evaluate_stack(self._symbol_stack[:])
        # Return appropriate message if error was encountered. Sometimes, we might want to print additional information to console.
        except exceptions.InputError as e:
            raise Exception("Input Error: " + e.message)
        except ZeroDivisionError:
            raise Exception("Arithmetic Error: Division by 0 is undefined.")
        except OverflowError:
            raise Exception("Error: Overflow error occured.")
        except ParseException:
            # Not using error message because it's unintuitive to non-technical users.
            raise Exception("Parsing Error: Invalid input entered.")
        except Exception as e:
            raise Exception("Evaluation Error: " + str(e))
