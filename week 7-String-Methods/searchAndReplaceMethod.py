
# these methods find charaters or strings inside other strings, or do replacements

#finds position of character
emailAddress = "james.filip.96@gmail.com"
userName = "GreenManaPlz"
print(emailAddress.find("@"))

#finds position of character AFTER a specified point
print(userName.find("n", 5))


userName = 'John?Doe?'
position = userName.find("Doe")

if position > -1:
    print("Username contains Doe")
#what if we want to retrieve the first part of an email, everything before "@" ?

#BAD, only works for this specific email
# using this slicing method, we need to hard code the range which isnt good
emailName = emailAddress[0 : 14]
print(emailName)

#GOOD, works for any email you enter
#using this method, the range is set to the entire string before "@"
emailName2 = emailAddress[0 : emailAddress.find("@")]
print(emailName2)

#this range will find the string content after the "@"
emailEnd = emailAddress[emailAddress.find("@") + 1 :  ]
print(emailEnd)


#this will replace unwated characters in a string with spaces
userName2 = "*GreenManaPlz*"
userName3 = userName2.replace("*", " ")
print(userName3)

#this will replace unwatec characters with no spaces
userName4 = userName2.replace("*", "")
print(userName4)


