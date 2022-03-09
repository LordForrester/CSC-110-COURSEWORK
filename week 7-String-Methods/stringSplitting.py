
# returns list of strings from another string, but seperated by ,
#the reason this works is because split returns the strings

studentLine = "123432, John Jones,29,350.78"
#this will create the list

studentFields = studentLine.split(",")
# printing the length of the list will display the number of strings in it

print(len(studentFields))
# now we can store them into varibles using indexing
studId = studentFields[0]

studName = studentFields[1]
studAge = int(studentFields[2])
studBal = float(studentFields[3])
print(studId, studName, studAge, studBal)
#we can also do this in a loop!

for studField in studentFields:
    print(studField)
    
def displayGroceryList(groceryString):
    groceryItems = groceryString.split(",")
    itemNum = 1
    for item in groceryItems:
        print(itemNum, item, sep="\t")
        itemNum += 1
displayGroceryList("apples, oranges, turkey bacon, cheese, skirt steak")

def displayGroceryList2(groceryString):
    groceryItems = groceryString.split(",")
    itemNum = 1
    for itemIndex in range(0, len(groceryItems)):
        print(itemIndex + 1, groceryItems[itemIndex], sep = "\t")
displayGroceryList2("apples, oranges, turkey bacon, cheese, skirt steak, (360) 936 - 3201")
