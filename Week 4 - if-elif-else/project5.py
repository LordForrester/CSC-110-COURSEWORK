#james filip 11/1/2021
import math
# emptRating returns string depending on the parameter given
def emptRating(rate):
    rating = ""
    if rate < 3:
        rating = "probation"
    elif rate < 5:
        rating = "Needs Improvement"
    elif rate < 8:
        rating = "Acceptable"
    elif rate < 10:
        rating = "Good"
    elif rate == 10:
        
        rating = "Excellent"
    else:
        rating = "ERROR"

    return rating

# test 1: I tested these numbers " 4, 6, 7", results were correct
# test 2: Also tested -1, output was still probabtion, possibly could fix to not allow numbers lower than 1 to be inputed.
# test 3: tested 11, returns "error"

# pctToNsc calculates the gpa with the given grade percent
    #if grade percent is 97 or higher, gpa does not exceed 4.0
def pctToNsc(gradePercent):
    
    NSC = ((gradePercent - 60) / 10) + .4
    
    if NSC < 1.0:   
        NSC = 0
    elif gradePercent < 1 or gradePercent > 100:
        NSC = -9.9
    elif gradePercent >= 97 and gradePercent <= 100:
        NSC = 4.0
        
    return NSC
# test 1: tested 0.9, result was 0. tested 101, result was -9.9. output correct
# test 2: tested 96, 97, 98, 99, 100. output was 4.0 

# isDivisibleBy5or7or11 returns a true or false value
#   depending on whether or not the given parameter is divisible by 5, 7, or 11
def isDivisibleBy5or7or11(integer):
    
    if integer % 5 == 0 or integer % 7 == 0 or integer % 11 == 0:
        divisible = True

    else:
        divisible = False
    return divisible

# test 1: tested numbers 5, 10, 11, 7, 14, 15, 11, 22, 23. output was as expected

# commission calculates the total commision earnings using the position, in sales, out sales, and worked months parameters
def commission(position, insales, outsales, numMonths):

    bump = 0
    
    if numMonths < 24:
        bump = 0
    elif numMonths <= 47:
        bump = .01
    elif numMonths <= 119:
        bump = .02
    else:
        bump = .03
    
    if position == "Trainee":
        
        commision = (insales  * .01) + (outsales * .02)
        
        
    elif position == "Associate":
        commision = (insales  * .03) + (outsales * .05)
        
        
        
    elif position == "Lead":
        commision = (insales  * .04) + (outsales * .06)
        
        
    elif position == "Manager":
        commision = (insales  * .05) + (outsales * .08)
        
    fullCommision = commision + (commision * bump)
    
    return fullCommision
# test 1: tested numMonths with 23, 24, 25, 46, 47, 48, 118, 119, 200. output as expected
# test 2: tested each role, all calculations being performed correctly
# test 3: tested set of parameters from assignment
# For example,  an Associate with in-state  sales of $4,000 and out-of-state  sales of $5,000, who has been 
    # with the company for 36 months would get a commission check of $373.70. output as expected
        
# main calls all functions


def main():
    print(emptRating(5))
    print(pctToNsc(95))
    print(isDivisibleBy5or7or11(28))
    print(commission("Associate", 4000, 5000, 36))
    

main()

#summary: overall, I learned how to properally use if, elif and else statements from this project.
