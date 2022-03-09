print('Employee Records Menu\n')
print('1.  Search for employee')
print('2.  Add employee')
print('3.  Delete employee')
print('0.  Exit')

menuChoice = int(input("Enter menu choice: "))
while menuChoice not in range(0, 4):
    menuChoice = int(input("Invalid; enter menu choice: "))

print("You entered valid menu choice of", menuChoice)
