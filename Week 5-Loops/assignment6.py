def inputLoanData():
    loanAmount      = int(input("Enter Loan Amount: "))
    while loanAmount < 0:
        print("No Negative Amounts")
        loanAmount      = int(input("Enter Loan Amount: "))
    ratePerPeriod   = float(input("Enter annual interest rate: ")) * .01 / 12
    while ratePerPeriod < 0:
        print("No Negative Rates")
        ratePerPeriod   = float(input("Enter annual interest rate: ")) * .01 / 12
    return loanAmount, ratePerPeriod
def showMenu():
    loanPeriods = -99
    print("-" * 50)
    print("  Mid-America Mortgage - Loan report menu")
    print("-" * 50)
    print("1.  15-year loan")
    print("2.  30-year loan")
    print("0.  EXIT")
    print()
    userChoice = int(input("Choice: "))
    while userChoice not in range(0, 3):
        print ("1.  15-year loan")
        print ("2.  30-year loan")
        print ("0.  EXIT")
        print()
        userChoice  = int(input("Choice: "))
    if userChoice   ==  0:
        loanPeriods =   0
    elif userChoice ==  1:
        loanPeriods =   15 * 12
    else:
        loanPeriods =   30 * 12
    return loanPeriods
def payment(pv, ratePerPeriod, numPeriods):
    payment = ratePerPeriod * pv / (1 - (1 + ratePerPeriod) ** -numPeriods)
    return round(payment, 2)
def showReport(pv, ratePerPeriod, numPeriods, paymentAmount):
    counter     = 0
    interestSum = 0 
    paymentSum  = 0
    
    print(format("Pmt#", "8s"), format("PmtAmt", "13s"), format("Int", "10s"), format("princ", "10s"), format("Balance", "10s"))
    print(format("-" * 4, "5s"), format("-" * 9, "14s"), format("-" * 5, "11s"), format("-" * 6 , "10s"), format("-" * 8, "10s"))
    
    
    for payment in range(numPeriods - 1):
        counter = counter + 1 
        interest = round(pv * ratePerPeriod, 2)
        interestSum+= interest
        paymentSum+= paymentAmount
        principal = round(paymentAmount - interest, 2)
        pv = pv - principal
        balance = round(pv, 2)
        
        print(format(counter, "4"), format(paymentAmount, "10.2f"), format(interest, "10.2f"), format(principal, "12.2f"), format(balance, "12.2f"))
        if counter % 12 == 0:
            print("-" * 50)
    counter+= 1
    interest = round(pv * ratePerPeriod, 2)
    paymentAmount = balance + interest
    interestSum+= interest
    paymentSum+= paymentAmount
    principal     = round(paymentAmount - interest, 2)
    pv            = pv - principal
    if pv < 0:
        pv = 0
    balance       = round(pv, 2)
    print(format(counter, "4"), format(paymentAmount, "10.2f"), format(interest, "10.2f"), format(principal, "12.2f"), format(balance, "12.2f"))
    print("-" * 50)
    print()
    print("Total of payments: $ \t", format(paymentSum, ",.2f"))
    print("Interest paid: $ \t", format(interestSum, ",.2f"))
    print()
    input("Press <Enter> to continue")
def main():
    periods  = -99
    pv, rate = inputLoanData()
    while periods != 0:
        periods   = showMenu()
        payAmount = payment(pv, rate, periods)
        showReport(pv, rate, periods, payAmount)
main()

#Summary
#I approached this Assignment by making sure each of the functions were properally doing there job
#   and calculating values correctly
#I was stuck when coding the payment function, I was having trouble understanding how the
#   formula needed to be coded and how the values needed to be convereted in the
#       inputLoanData function before calculation.
#I also had trouble in the showReport function when coding the last line of data.
#   I chose the option of looping by the number of periods - 1 so that I can handle the last line of output outside the loop. 

#Test 1: Input loanData working correctly, (however by that time I did not realized that I needed to convert the values further)
#Test 2: testing showMenu() to make sure the function would continue to loop unless
# the user enters 0, 1 or 2. loops accordingly
#Test 2: payment() not calculating correctly. I make edits to the paranthesis.
#Test 3: payment output still incorrect. I finally realize that I need to convert the outputs in inputLoanData "* .01 / 12"
#Test 4: payment output is finally correct..probably.
#Test 5: After spending time figuring out when AND where to increment interestSum and paymentSum in showReport(),
#   the data output was correct after each loop, except for the last of course.
#       I take the route of changing the loop range to equal the amount of payment periods - 1. and printing the final line of output outside the loop

#Test 6: after changing the loop range, the show data function was working properaly. but the 0.00 in the last line of balance data was
#   displaying as "-0.00".
#Test 7: after realizing that the showReport function was rounding negative values, I decide to edit the last line of output to convert
#   a negative pv value to 0.
#Test 8: Output looks correct. I attempt extra credit loop validations with no issues either. 
