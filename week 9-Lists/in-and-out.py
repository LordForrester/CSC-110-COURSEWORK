vowels = "AEIOU"
print("x" in vowels)

print("U" in vowels)




cakeBatterIngreds = ['butter', 'sugar', 'baking poweder', \
                     'vanilla', 'egg', 'flour', 'milk']


pieDoughIngreds = ['flour', 'salt', 'water', 'butter']
pastaDoughIngreds = ['flour', 'egg', 'olive oil']

#.lower allows the input to be any case
sensIngred = input("Enter an ingredient: ").lower()
print("Here are the recipes that are safe for you")

# if the userInput is inside any of the lists, that food type wont show up
# in the output as a safe food
if sensIngred not in cakeBatterIngreds:
    print("Cake batter is safe!")

if sensIngred not in pieDoughIngreds:
    print("Pie dough is safe!")

if sensIngred not in pastaDoughIngreds:
    print("Pasta dough is safe!")
