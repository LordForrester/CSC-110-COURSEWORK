# input

userName = input("What is your name? ")

subtotal = float(input("What is the subtotal? "))
# processing
# calculate tax :subtotal x 0.95

tax = subtotal * 0.095


#output

print("\nHello", userName, "here is your sales information:\n")

print("Subtotal = $", format(subtotal,       "9,.2f"))

print("     Tax = $", format(tax,            "9,.2f"))

print("            ", "-" *                   9)

print("   Total = $", format(subtotal + tax, "9,.2f"))
