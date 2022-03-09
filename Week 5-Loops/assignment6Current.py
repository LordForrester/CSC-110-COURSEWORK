def inputLoanData():
    loanAmount      = int(input("Enter Loan Amount: "))
    while loanAmount < 0:
        loanAmount      = int(input("Enter Loan Amount: "))
    ratePerPeriod   = float(input("Enter annual interest rate: ")) * .01 / 12
    while ratePerPeriod < 0:
        ratePerPeriod   = float(input("Enter annual interest rate: ")) * .01 / 12
    return loanAmount, ratePerPeriod
def showMenu():
    loanPeriods = -99
    print("-" * 50)
    print("Mid-America Mortgage - Loan report menu")
    print("-" * 50)
    print("1.  15-year loan")
    print("2.  30-year loan")
    print("0.  EXIT")
    userChoice = int(input("Choice: "))
    while userChoice not in range(0, 3):
        print ("1.  15-year loan")
        print ("2.  30-year loan")
        print ("0.  EXIT")
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
    
    print("Pmt", "PmtAmt", "Int", "princ")
    for payment in range(numPeriods - 1):
        counter = counter + 1 
        interest = round(pv * ratePerPeriod, 2)
        interestSum+= interest
        paymentSum+= paymentAmount
        principal = round(paymentAmount - interest, 2)
        pv = pv - principal
        balance = round(pv, 2)
        
        print(format(counter, "4"), format(paymentAmount, "10.2f"), format(interest, "9.2f"), format(principal, "12.2f"), format(balance, "12.2f"))
        if counter % 12 == 0:
            print("-" * 50)
    counter+= 1
    interest = round(pv * ratePerPeriod, 2)
    paymentAmount = balance + interest
    interestSum+= interest
    paymentSum+= paymentAmount
    principal     = round(paymentAmount - interest, 2)
    pv            = pv - principal
    balance       = round(pv, 2)
    (format(counter, "4"), format(paymentAmount, "10.2f"), format(interest, "9.2f"), format(principal, "12.2f"), format(balance, "12.2f"))
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

#test 1: 
