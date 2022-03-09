#These are string methods; they take the form string.method()

# .is___ methods test a string and return a true or false result

#isspace finds white space, not just spaces

userName = " james"
hasSpace = False
for char in userName:
    if char.isspace():
        hasSpace = True

if hasSpace == True:
    print("Username has at least one space in it")
