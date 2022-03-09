#best practice for processing in all languages

def totalAndAvg(theList):
    tot = 0.0
    for aNum in theList:
        tot += aNum
    avg = tot / len(theList)
    return tot, avg

print()


def minAndMax(theList):
    min = theList[0]
    max = theList[0]
    for aNum in theList:
        if aNum < min:
            min = aNum
        if aNum > max:
            max = aNum
    return min, max
