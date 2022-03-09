myFriends = ['Dana', 'Pat', 'Chris', 'Lupe']

myFriends.append(42)

print(myFriends)

#myFriends.sort()

#trying to sort will drop an error because the 42 we added is an int not a 'str'
#   to fix this, we can change it

myFriends[-1] = str(myFriends[-1])

myFriends.sort()

print(myFriends)

# also you can use .sort(reverse = True) for a reverse sort

myFriends.sort(reverse = True)

print(myFriends)
