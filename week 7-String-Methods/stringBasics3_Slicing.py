#concatenation
firstName = "James"
lastName = "Filip"

wholeName = firstName + " " + lastName

print(wholeName)

#immutability
name = "james"

name = "mr. " + name

print(name)

userName = "James Filip"

#Whole string (no start or end specified)
print(userName[:])

#Substring; up to but not includingindex 5
print(userName[0:5])

#Rest of string starting at index6
print(userName[6:])

#Rest of string starting 5 back from end
print(userName[-5:])

#Beginningof string through just beforeindex 5
print(userName[:5])

#Everyother character (step value of 2)
print(userName[0::2])
