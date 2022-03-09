
myFriends = ["Jon", "Rob", "Ned", "Arya", "Sansa"]

# prints the length of a list
print(len(myFriends))

#print anywhere in a list
print(myFriends[1])
print(myFriends[-1])
print(myFriends[-5])

rangeList = list(range(1, 11))

print(rangeList)

friend1 = "Tyrion"
friend2 = "Jamie"
friend3 = "Tywin"

myWorstFriends = [friend1, friend2, friend3]

print(myWorstFriends)

for oneFriend in myFriends:
    print(oneFriend)

#you can also change the contents of a list

myFriends[0] = "Aemon"

print(myFriends)

# you can also set ranges with lists

myListRange = myFriends[1 : 3]

print(myListRange)

allFriends = myFriends + myWorstFriends

print(allFriends)
