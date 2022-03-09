def drawWideBox(boxWidth):
    
    print("+", "-" * (boxWidth - 2), "+", sep = "")
    
    print("|", " " * (boxWidth - 2), "|", sep = "")
    
    print("|", " " * (boxWidth - 2), "|", sep = "")

    print("+", "-" * (boxWidth - 2), "+", sep = "")


def main():

    myBoxWidth = int(input("What box width? "))

    drawWideBox(myBoxWidth)


    main()
