!pip install sympy

import sympy as smp
from sympy import *

x, y = smp.symbols('x y')

f = x**2 + y

f.subs(x,y)

