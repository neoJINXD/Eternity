from flask import Flask
functions = Flask(__name__)

from .common import *
from .exponents_and_logs import *
from .sin import *
from .statistic import *
from .trignometry import *
