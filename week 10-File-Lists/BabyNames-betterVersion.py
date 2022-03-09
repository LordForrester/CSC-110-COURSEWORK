babyNameFile = open("BabyNames2015.txt", 'r')
#readlines() reads all the lines in a file and returns them as a list of strings
babyNameList = babyNameFile.readlines()
babyNameFile.close


for nameIndex in range(0, len(babyNameList)):
    babyNameList[nameIndex] = babyNameList[nameIndex].strip()
    
print(babyNameList)
    
babyNameList.sort()   

sortedNameFile = open("BabyNames2015-Sorted.txt", "w")
allNames = "\n".join(babyNameList)
sortedNameFile.write(allNames)
sortedNameFile.close()
  

# join string method, opposite of split. It takes a list and generates a string

