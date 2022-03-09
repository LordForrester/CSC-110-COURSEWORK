import random

def rollDie():
    return random.randrange(1, 6 + 1)

def rollDieUntil(target):
    print("Your target roll is", target)
    roll = -9
    while roll != target:
        roll = rollDie()
        print("You rolled a", roll)
    print("Your hit the target!")

def main():
    rollDieUntil(rollDie())

main()
