babyNameList = []
babyNameFile = open("BabyNames2015.txt", 'r')

for babyName in babyNameFile:
    babyNameList.append(babyName.strip())
babyNameFile.close

babyNameList.sort()
print(babyNameList)


sortedNameFile = open("BabyNames2015-Sorted.txt", "w")
for babyName in babyNameList:
    sortedNameFile.write(babyName + "\n")
sortedNameFile.close()
  
