import math

def circleCircum(rad):

    circumference = round(2 * math.pi * rad, 2)
    return circumference

   
def circleArea(rad):
    
    area = round(math.pi * rad ** 2, 2)
    return area


def sphereVolume(rad):
    
    volume = round(4 / 3 * math.pi * rad ** 3, 2)
    return volume


def sphereArea(rad):

    area = round(4 * math.pi * rad ** 2, 2)
    return area


def squarePerimiter(side):

    perimiter = round(4 * side, 2)
    return perimiter


def squareArea(side):

    area = round(side ** 2, 2)
    return area


def cubeVolume(side):

    volume = round(side ** 3, 2)
    return volume

def cubeArea(side):
    area = round(6 * side ** 2, 2)
    return area










