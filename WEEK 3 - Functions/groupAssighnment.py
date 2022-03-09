PAY_FORMAT = "13s"

def userInput():
    name = input("What is your name? ")
    hoursWorked = float(input("How many hours did you work? "))
    hourlyWage = float(input("What's your hourly wage? "))
    deduct = int(input("How many deductions have you gotten? "))
    return name, hoursWorked, hourlyWage, deduct

def calcGross(hours, wage):
    return hours * wage
    
def calcSS(grossPay):
    return grossPay * 0.062

def calcMed(grossPay):
    return grossPay * 0.0145

def calcWith(deduct):
    return ((80.8 * deduct) * .2)

def payStub(name, grossPay, ssTax, medTax, withTax, netPay):
    print("Check for", name)
    print("-" * 30)
    print("Gross Pay", format(grossPay, ">30.2f"))
    print("SS Tax", format(ssTax, ">30.2f"))
    print("Medicare Tax", format(medTax, ">30.2f"))
    print("Withholding", format(withTax, ">30.2f"))
    print("-" * 30)
    print("Net Pay", format(netPay, ">30.2f"))
def main():
    name, hoursWorked, hourlyWage, deduct = userInput()
    grossPay = calcGross(hoursWorked, hourlyWage)
    ssTax = calcSS(grossPay)
    medTax = calcMed(grossPay)
    withTax = calcWith(deduct)
    netPay = grossPay - ssTax - medTax - withTax

    payStub(name, grossPay, ssTax, medTax, withTax, netPay)

    print(grossPay)
    print(ssTax)
    print(medTax)
    print(withTax)
    
main()
