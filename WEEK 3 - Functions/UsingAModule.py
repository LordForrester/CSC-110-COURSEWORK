# method 1 - import module, use functions in this form
#           moduleName.functionName
#import math

#print(math.sqrt(82) * math.pi)

#method 2 - import functions you want from module,
#           use them directly

#from math import sqrt
#from math import pi
#print(sqrt(82)* pi)

# method 3 - import all functions from module,
#           use them directly
#from math import *
#print(sqrt(82) * pi)

from taxFunctions import TAX_RATE
from taxFunctions import calcTax
print(TAX_RATE)
print(calcTax(342.79))
