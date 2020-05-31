__source__ = '''
https://github.com/pyparsing/pyparsing/blob/master/examples/fourFn.py
'''
__note__ = '''
Demonstration of the pyparsing module, implementing a simple 4-function expression parser,
with support for scientific notation, and symbols for e and pi.
Extended to add exponentiation and simple built-in functions.
Extended test cases, simplified pushFirst method.
Removed unnecessary expr.suppress() call (thanks Nathaniel Peterson!), and added Group
Changed fnumber to use a Regex, which is now the preferred method
Reformatted to latest pypyparsing features, support multiple and variable args to functions
use % as op must change the logic
'''
#%%
from pyparsing import (
    Literal,
    Word,
    Group,
    Forward,
    alphas,
    alphanums,
    Regex,
    ParseException,
    CaselessKeyword,
    Suppress,
    delimitedList,
)
import math
import operator
from .calculation import Calculation

class Parser(object):
    exprStack = []
    def pushFirst(self, strg, loc, toks):
        self.exprStack.append(toks[0])

    def pushUMinus(self, strg, loc, toks):
        for t in toks:
            if t == "-":
                self.exprStack.append('unary -')
            else:
                break

    def __init__(self):
        cal = Calculation()        

        """
        expop   :: '^'
        multop  :: '*' | '/'
        addop   :: '+' | '-'
        integer :: ['+' | '-'] '0'..'9'+
        atom    :: PI | E | real | fn '(' expr ')' | '(' expr ')'
        factor  :: atom [ expop factor ]*
        term    :: factor [ multop factor ]*
        expr    :: term [ addop term ]*
        """
        # use CaselessKeyword for e and pi, to avoid accidentally matching
        # functions that start with 'e' or 'pi' (such as 'exp'); Keyword
        # and CaselessKeyword only match whole words
        e = CaselessKeyword("E")
        pi = CaselessKeyword("PI")
        # fnumber = Combine(Word("+-"+nums, nums) +
        #                    Optional("." + Optional(Word(nums))) +
        #                    Optional(e + Word("+-"+nums, nums)))
        # or use provided pyparsing_common.number, but convert back to str:
        # fnumber = ppc.number().addParseAction(lambda t: str(t[0]))
        fnumber = Regex(r"[+-]?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?")
        ident = Word(alphas, alphanums + "_$")

        plus, minus, mult, div = map(Literal, "+-*/")
        lpar, rpar = map(Suppress, "()")
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")

        expr = Forward()
        expr_list = delimitedList(Group(expr))
        # add parse action that replaces the function identifier with a (name, number of args) tuple
        def insert_fn_argcount_tuple(t):
            fn = t.pop(0)
            num_args = len(t[0])
            t.insert(0, (fn, num_args))

        fn_call = (ident + lpar - Group(expr_list) + rpar).setParseAction(
            insert_fn_argcount_tuple
        )
        atom = (
            addop[...]
            + (
                (fn_call | pi | e | fnumber | ident).setParseAction(self.pushFirst)
                | Group(lpar + expr + rpar)
            )
        ).setParseAction(self.pushUMinus)

        # by defining exponentiation as "atom [ ^ factor ]..." instead of "atom [ ^ atom ]...", we get right-to-left
        # exponents, instead of left-to-right that is, 2^3^2 = 2^(3^2), not (2^3)^2.
        factor = Forward()
        factor <<= atom + (expop + factor).setParseAction(self.pushFirst)[...]
        term = factor + (multop + factor).setParseAction(self.pushFirst)[...]
        expr <<= term + (addop + term).setParseAction(self.pushFirst)[...]
        self.bnf = expr

        # map operator symbols to corresponding arithmetic operations
        epsilon = 1e-12
        eps = 1e-3
        self.opn = {"+": operator.add,
                    "-": operator.sub,
                    "*": operator.mul,
                    "/": operator.truediv,
                    "^": operator.pow,}
        self.fn = {"sinh": math.sinh,
                   "cosh": math.cosh,
                   "tanh": math.tanh,
                    "sin": math.sin,
                    "cos": math.cos,
                    "tan": math.tan,
                    "exp": math.exp,
                    "abs": abs,
                    "trunc": int,
                    "round": round,
                    "sgn": lambda a: -1 if a < -epsilon else 1 if a > epsilon else 0,
                    # functionsl with multiple arguments
                    "multiply": lambda a, b: a * b,
                    "hypot": math.hypot,
                    # functions with a variable number of arguments
                    "all": lambda *a: all(a),
                    "mod": operator.mod,
                    "mad": cal.mad,
                    "std": cal.std,}

    def evaluateStack(self, s):
        op, num_args = s.pop(), 0
        if isinstance(op, tuple):
            op, num_args = op
        if op == 'unary -':
            return -self.evaluateStack(s)
        if op in "+-*/^":
            op2 = self.evaluateStack(s)
            op1 = self.evaluateStack(s)
            return self.opn[op](op1, op2)
        elif op == "PI":
            return math.pi  # 3.1415926535
        elif op == "E":
            return math.e  # 2.718281828
        elif op in self.fn:
            # note: args are pushed onto the stack in reverse order
            args = reversed([self.evaluateStack(s) for _ in range(num_args)])
            return self.fn[op](*args)
        elif op[0].isalpha():
            raise Exception("invalid identifier '%s'" % op)
        else:
            # try to evaluate as int first, then as float if int fails
            try:
                return int(op)
            except ValueError:
                return float(op)

    def eval(self, num_string, expected=None, parseAll=True):
        self.exprStack[:] = []
        try:
            results = self.bnf.parseString(num_string, parseAll)
            val = self.evaluateStack(self.exprStack[:])
        except ParseException as pe:
            print(num_string, "failed parse:", str(pe))
            return "Error: Unknown input character."
        except Exception as e:
            print(num_string, "failed eval:", str(e), self.exprStack)
            return "Error: Unknown input character."
        else:
            if expected is None:
                return val
            else:
                if val == expected:
                    print(num_string, "=", val)
                    return val
                else:
                    print(num_string + "=", val, " != ", expected, results, "=>", self.exprStack)       

# # %%
# nsp = Parser()
# result = nsp.eval("(9+3) / 11", (9 + 3.0) / 11)
# print(result)

# # %%
# nsp = Parser()
# result = nsp.eval("sin(PI/2)", 1)
# print(result)

# # %%
# nsp = Parser()
# result = nsp.eval("mad(3, 15, 21, 13)", 5)
# print(result)

# # %%
# nsp = Parser()
# result = nsp.eval("5%3", 2)
# print(result)
