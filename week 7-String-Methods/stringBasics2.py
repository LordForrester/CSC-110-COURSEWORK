userName = "James"
#The first character is position 0, not 1; the last character is one less tahn length
firstCh = userName[1]
lastCh = userName[len(userName) - 1]
#Indexing using nevagtives will count from the end of the string, where -1 is the last character
alsoLastCh = userName[-1]

print(firstCh)
print(lastCh)
print(alsoLastCh)
