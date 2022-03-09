myFriends = ['Dana', 'Pat', 'Chris', 'Lupe']

# will print the index number for Chris
print(myFriends.index("Chris"))

#Will print true or false if this name is in the list
print("Xander" in myFriends)

myFriends2 = ['Chris', 'Dana', 'Pat', 'Chris', 'Lupe', 'Chris']

#Will print the count of this name in this list
print(myFriends2.count('Chris'))


# will add name to end of list

myFriends.append('Morgan')

print(myFriends)

# insert will add to a spot in the list you choose
myFriends.insert(0, "James")
myFriends.insert(4, "Derek")
myFriends.insert(5, "Derek")

myFriends.insert(-1, "Tony")

print(myFriends)

# remove will remove a name from the list
myFriends.remove("Derek")
print(myFriends)

myOneFriend = ['Chris', 'Dana', 'Pat', 'Chris', 'Lupe', 'Chris', 'Chris', 'Chris']
# sort will sort the list by letter
myFriends.sort()
print(myFriends)

print(myOneFriend.count("Chris"))

while myOneFriend.count("Chris") > 1:
    myOneFriend.remove("Chris")
print(myOneFriend.count("Chris"))



