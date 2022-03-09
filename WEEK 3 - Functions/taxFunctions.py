TAX_RATE = 0.11

def calcTax(saleAmount):
    tax = round(saleAmount * TAX_RATE, 2)
    return tax

