def drawSquare(sideLength):
    forward(sideLength)
    right(90)
    forward(sideLength)
    right(90)
    forward(sideLength)
    right(90)
    forward(sideLength)
    right(90)

def drawWindow(paneSize):
    drawSquare(paneSize)
    left(90)
    drawSquare(paneSize)
    left(90)
    drawSquare(paneSize)
    left(90)
    drawSquare(paneSize)
    left(90)

def getUserOptions():
    userColor =        input("What color? ")
    userPenSize = int( input("What pen size? " ))
    userPaneSize = int(input("What pane size? "))
    return userColor, userPenSize, userPaneSize

def main():
    whatColor, whatPenSize, whatPaneSize = getUserOptions()
    color(whatColor)
    pensize(whatPenSize)
    drawWindow(whatPaneSize)
    done()

from turtle import *
main()
