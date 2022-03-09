#James Filip
#10/17/21
#This program generates a template for programs

#these constants make formatting easier
bannerWidth = ("#" + "*" * 75)
newLine = "\n\n"

#returned data
name =  ""
date = ""
program = ""
descrip = ""


#Collect inputs will return inputed data to the values above 
def collectInputs():
    global name, date, program, descrip
    name = input("Enter your Name: ")
    date = input("Enter the date: ")
    program = input("Enter the program name: ")
    descrip = input("Enter short description: ")
    
#Formats the UI for the program
def displayBanner():
    displayStarLine()
    print("#\tCoder\t:\t", name)
    print("#\tDate\t:\t", date)
    print("#\tProgram\t:\t", program)
    print("#\tDescrip\t:\t", descrip)
    displayStarLine()
    print(newLine)

#generates line of stars
def displayStarLine():
    print(bannerWidth)

#creates the template 
def displaySectHeaders():
    displaySectHeader("#\tConstants")
    displaySectHeader("#\tVariables")
    displaySectHeader("#\tInput")
    displaySectHeader("#\tProcessing")
    displaySectHeader("#\tOutput")
    

#formats alignment 
def displaySectHeader(sectionName):
    displayStarLine()
    print(sectionName)
    displayStarLine()
    print (newLine)

#calls all other functions
def main():
    collectInputs()
    displayBanner()
    displaySectHeaders()

main()

#Test 1: I tested to make sure the inputed data was showing up, It was not. I corrected this by adding: global name, date, program, descrip, to the collectInputs function
#Test 2: I was not sure how to futher test the program other than to make sure the spacing and alighment correctly happening, I had no issues

#Summary: The program worked as expected after correcting the collectInputs function. Overallm this project helped me to understand how global variables work. 
