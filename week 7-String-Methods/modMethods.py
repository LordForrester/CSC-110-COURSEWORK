#Also removes white spaces from start or end of strings
userName = " John Doe    \t \n"
userName = userName.strip()
# spe='' with removing seperation between "- John Doe -"
print('-', userName, '-', sep='')

#removes characters
# this ONLY works at the start and/or end; middle characters require other methods

print('!Hello!' .strip('!'))

groceryItem = 'Green Beans'
#all lower case
print(groceryItem.lower())
#all upper case
print(groceryItem.upper())
#capitalize first letter of first word
print(groceryItem.capitalize())
#switch case of letters in string
print(groceryItem.swapcase())

# returns word with capitalization, ignoring " \t" and "\n"
def formatWord(word):
    userName = word
    userName = userName.strip()
    userName = userName.strip('+')
    userName = userName.upper()
    
    print(userName)
formatWord('   \t+hello+\n  ')

#faster option
def formatWord2(word):
    word =word.strip().strip('+').upper()
    print(word)
formatWord2('   \t+hello+\n  ')







