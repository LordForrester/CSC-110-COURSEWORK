import math

numCustomers = int(input("How many people to be served? "))

# to make my batch counter, I divide the number of people inputed by 12,
#   and use math.ceil to round up another batch 
BATCHES = math.ceil(numCustomers / 12)


# i create constants to help make conversion easier
COCOA_GRAMS_PER_BATCH = 106
COCOA_OUNCES_PER_CONTAINER = 8

SALT_GRAMS_PER_BATCH = 6
SALT_OUNCES_PER_CONTAINER = 26

BAKINGPOW_GRAMS_PER_BATCH = 5
BAKINGPOW_OUNCES_PER_CONTAINER = 8.1

ESPRESSOPOW_GRAMS_PER_BATCH = 2
ESPRESSOPOW_OUNCE_PER_CONTAINER = 7.05

SUGAR_GRAMS_PER_BATCH = 447
SUGAR_POUNDS_PER_CONTAINER = 4

FLOUR_GRAMS_PER_BATCH = 180
FLOUR_POUNDS_PER_CONTAINER = 5

CHOCOLATE_GRAMS_PER_BATCH = 340
CHOCOLATE_OUNCES_PER_CONTAINER = 12

BUTTER_POUNDS_PER_BATCH = .5
BUTTER_POUNDS_PER_CONTAINER = 1

VANILLA_TBSP_PER_BATCH = 1
VANILLA_OUNCES_PER_CONTAINER = 2

EGGS_PER_BATCH = 4
EGGS_PER_CONTAINER = 18




GRAMS_IN_OUNCE = 28.3495231
OUNCES_IN_POUND = 16
#Instead of trying to convert vanilla tablesoons to teaspoons to cups to ounces, I just used the ammount of tbsp in 1 ounce 
TBSP_IN_OUNCE = 2


#To count cocoa ounces, I multiply the 106 by the number of batches calculated,
#   and divide that by the ammount of grams in 1 ounce

#to count the ammount of containers needed, i divide the ammount of ounces calculated by the number of ounces in a cocoa container
COCOA_OUNCE = (COCOA_GRAMS_PER_BATCH * BATCHES) / GRAMS_IN_OUNCE
COCOA_CONTAINER = math.ceil(COCOA_OUNCE / COCOA_OUNCES_PER_CONTAINER)
COCOA_PRICE = (COCOA_CONTAINER * 1.99)

SALT_OUNCE = (SALT_GRAMS_PER_BATCH * BATCHES) / GRAMS_IN_OUNCE
SALT_CONTAINER = math.ceil(SALT_OUNCE / SALT_OUNCES_PER_CONTAINER)
SALT_PRICE = (SALT_CONTAINER * 0.49)

BAKINGPOW_OUNCE = (BAKINGPOW_GRAMS_PER_BATCH * BATCHES) / GRAMS_IN_OUNCE
BAKINGPOW_CONTAINER = math.ceil(BAKINGPOW_OUNCE / BAKINGPOW_OUNCES_PER_CONTAINER)
BAKINGPOW_PRICE = (BAKINGPOW_CONTAINER * 1.89)

ESPRESSOPOW_OUNCE = (ESPRESSOPOW_GRAMS_PER_BATCH * BATCHES) / GRAMS_IN_OUNCE
ESPRESSOPOW_CONTAINER = math.ceil(ESPRESSOPOW_OUNCE / ESPRESSOPOW_OUNCE_PER_CONTAINER)
ESPRESSOPOW_PRICE = ESPRESSOPOW_CONTAINER * 5.39


SUGAR_OUNCE = (SUGAR_GRAMS_PER_BATCH * BATCHES) / GRAMS_IN_OUNCE
SUGAR_POUNDS = SUGAR_OUNCE / OUNCES_IN_POUND
SUGAR_CONTAINER = math.ceil(SUGAR_POUNDS / SUGAR_POUNDS_PER_CONTAINER)
SUGAR_PRICE = SUGAR_CONTAINER * 1.99

FLOUR_OUNCE = (FLOUR_GRAMS_PER_BATCH * BATCHES) / GRAMS_IN_OUNCE
FLOUR_POUNDS = FLOUR_OUNCE / OUNCES_IN_POUND
FLOUR_CONTAINER = math.ceil(FLOUR_POUNDS / FLOUR_POUNDS_PER_CONTAINER)
FLOUR_PRICE = FLOUR_CONTAINER * 1.99

CHOCOLATE_OUNCE = (CHOCOLATE_GRAMS_PER_BATCH * BATCHES) / GRAMS_IN_OUNCE
CHOCOLATE_CONTAINER = math.ceil(CHOCOLATE_OUNCE / CHOCOLATE_OUNCES_PER_CONTAINER)
CHOCOLATE_PRICE = CHOCOLATE_CONTAINER * 1.99

BUTTER_POUNDS = BUTTER_POUNDS_PER_BATCH * BATCHES
BUTTER_CONTAINER = math.ceil(BUTTER_POUNDS / BUTTER_POUNDS_PER_CONTAINER)
BUTTER_PRICE = BUTTER_CONTAINER * 2.99

VANILLA_OUNCE = (VANILLA_TBSP_PER_BATCH * BATCHES) / TBSP_IN_OUNCE
VANILLA_CONTAINER = math.ceil(VANILLA_OUNCE / VANILLA_OUNCES_PER_CONTAINER)
VANILLA_PRICE = VANILLA_CONTAINER * 10.59

EGGS = EGGS_PER_BATCH * BATCHES
EGG_CONTAINER = math.ceil(EGGS / EGGS_PER_CONTAINER)
EGG_PRICE = EGG_CONTAINER * 1.99


TOTAL_COST = (COCOA_PRICE + SALT_PRICE + BAKINGPOW_PRICE + ESPRESSOPOW_PRICE + SUGAR_PRICE + FLOUR_PRICE + CHOCOLATE_PRICE + BUTTER_PRICE + VANILLA_PRICE + EGG_PRICE)




print ("\n\nTo serve", numCustomers, "make", BATCHES, "batches\n")
print ("-" * 30)
print (format("Grocery List", "^30s"))
print ("-" * 30)

print (format("Cocoa", '25s'),COCOA_CONTAINER)
print (format("Salt", '25s'),SALT_CONTAINER)
print (format("Baking Powder", '25s'),BAKINGPOW_CONTAINER)
print (format("Espresso Powder", '25s'),ESPRESSOPOW_CONTAINER)
print (format("Sugar", '25s'),SUGAR_CONTAINER)
print (format("Flour", '25s'),FLOUR_CONTAINER)
print (format("Chocolate", '25s'),CHOCOLATE_CONTAINER)
print (format("Butter", '25s'),BUTTER_CONTAINER)
print (format("Vanilla", '25s'),VANILLA_CONTAINER)
print (format("Eggs", '25s'),EGG_CONTAINER)



print ("\nTotal $ ", format(TOTAL_COST, "17,.2f"))

#Test 1: I tested the container counter by calculating how many batches can be
#   made using 1 container of cocoa powder.
#    since 1 batch uses 106 grams of cocoa powder and feeds 12,
#     and the 8 ounce container hold 226.79 grams of cocoa powder,
#      2 containers should be outputed if any number past > 24 is inputed by the user.
#       this is true when testing. and the testing method yielded consistent results
#         with every ingriedent container counter

#Test 2: I was having trouble formating the container ouputs so that they would line up accordingly
# I ended up needing to specifically specifiy the amount of space required per container
#   because the space taken up was different depending on the length of the string that follows it

#Summary: I struggled mainly with simplifying calculations by using constants instead of over calculating
#, but once I started using constants, I had a much more easy and simplictic time writing up
#   my calculations.
#    I learned that when analayzing the requirments for a python project,
#     its important to recognize what data is constantly being used, and what steps should be taken
#      to write a logical solution rather than a complex one.  








