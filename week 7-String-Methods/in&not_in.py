def containsVowels(string):
    #converting the string to uppercase will make sure the output is correct for lower and upper case entries
    string = string.upper()
    if "A" in string or "E" in string or "I" in string or "O" in string or "U" in string:
        return True
    

print(containsVowels("ass"))


def containsVowels2(string):
    string = string.upper()
    for vowel in "AEIOU":
        if vowel in string:
            return True
    return False

print(containsVowels2("Fly"))
