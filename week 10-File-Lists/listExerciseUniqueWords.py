def ageAtNextBirthday(currentAge):
    currentAge += 1

def addEndOfListMarker(aList):
    aList.append("--> end of list <--")
    aList[0] = "kombucha"
    aList.remove('pizza')

def main():
    userAge = 39
    print(userAge)
    ageAtNextBirthday(userAge)
    print(userAge)

    groceryList = ['cheese', 'eggs' 'brocolli' 'pizza' 'milk']
    print(groceryList)
    addEndOfListMarker(groceryList)
    print(groceryList)

if __name__ == '__main__':
    main()
