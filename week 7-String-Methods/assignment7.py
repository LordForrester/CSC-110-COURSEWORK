#James Filip
#11/19/2021

# replaces mistakable characters with correct ones. converts to int and returns
def fixCustNum(custNumber):
    custNumber = int(custNumber.replace("O", "0").replace("o", "0").replace("l", "1"). replace("'", ""))
    return int(custNumber)

# clears uneeded spacing between first and last names, returns last name and first name strings
def fixCustName(custName):
    custName  = custName.strip()
    lastName  = custName[0 : custName.find(",")]
    firstName = custName[custName.find(",") + 1 : ]
    firstName = firstName.strip()
    return lastName, firstName

# replaces enterable phone number characters with empty space, returns area and phone strings
def fixCustPhone(custPhone):
    custPhone = custPhone.replace("-", "").replace(")", "").replace("(", "").replace(" ", "")
    custArea  = custPhone[0 : 3]
    custPhone = custPhone[4 : ]
    return custArea, custPhone

# removes enterable currency characters with 
def fixCustBalance(custBalance):
# .strip("$") and .strip(",") will return a bug if used on a floating variable,
#   so convert to float AFTER using strip on them    
    custBalance = custBalance.strip("$")
    custBalance = custBalance.replace("'", "").replace(",", "").replace(" ", "")
    return float(custBalance)
    
def main():
    string    = input("Enter customer string: ")
    string    = string.split("#")
    print(("Customer number\t\t:")  , fixCustNum(string[0]))
    custName  = fixCustName(string[1])
    print(("Customer last name\t:") , custName[0])
    print(("Customer first name\t:"), custName[1])
    custPhone = fixCustPhone(string[2])
    print(("Customer area code\t:") , custPhone[0])
    print(("Customer phone\t\t:")   , custPhone[1])
    print(("Customer balance\t:")   , fixCustBalance(string[3]))
    
main()
#TEST CASE 1: '1O53l6#Lopez,  Lupe Luisa #(206)555-1845#$1,346.75'
# output works only if inputted as shown. "$", "," and "'" still appear however
# fixed balance output. balance shows correct output now

#TEST CASE 2: '1O53l6#Lopez,  Lupe Luisa #206)5551845#$1,346.75'
#output for customer phone and area is not correct. Realizing I need to change ranges to indexes
#output is now correct

#TEST CASE 3: '1O53l6#Lopez,  Lupe Luisa #  206)555  1845 #$  1,346.75  '
#output for cust phone and area not correct, realizing I need to replace any white space with ""
#output is now correct, same fix for balance

#TEST CASE 4: '  1O53l60123940129310490123  #    Lopez,  Lupe Luisa     #  206)555  1845 #$   1,346.75  '
#output is correct

 # I began this assignment my just making sure the functions were correctly
#   outputting the individuel parts of the string seperated by #, and worring about passing them later
# I got stuck first when I was trying to pass the specific sections of the string
#   to each function. I spent time thinking about ranges when I should have been
#   converting the string to a list and splitting by "#"
#I also got stuck when trying to use strip() in fixCustBalance, i did not realize that certain characters cannot be
#   removed from a floating point variable.
#I did not like that random spacing during the input would display or cause errors,
#   so I used strip() or replace(" ", "") to correct this
# I learned about handling strings in more useable and integratable ways. Making data presentable no matter how its entered feels very rewarding









