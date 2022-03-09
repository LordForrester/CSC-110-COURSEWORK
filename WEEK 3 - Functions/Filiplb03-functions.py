# Lab 3 starter code
# CSC 110

import math

def main():
    print("This program is to test functions")
    # put your function calls here
    print (areaTrapezoid(4, 5, 8))
    
    print (areaTrapezoid(2, 7, 9))

    print (areaHypoteneuse(58, 36))
    
    
    

   
  

# This function calculates and returns the area of a trapezoid
# parameter: base1, the length of the top of the trapezoid
# parameter: base2, the length of the bottom
# parameter: height, the height of the trapezoid
# See this website for a picture  http://math.com/tables/geometry/areas.htm
def areaTrapezoid(base1, base2, height):
    area = (height / 2.0 * (base1 + base2))
    return area

def areaHypoteneuse(legA, legB):
    hypoteneuse = round(math.sqrt(legA ** 2 + legB ** 2), 2)
    return hypoteneuse

main()
