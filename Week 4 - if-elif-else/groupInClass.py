haveDiploma  =       input("Have diploma (Y/N): ")
haveGed      =       input("Have GED (Y/N): ")
readyForFall =       input("Able to start in Fall 2021 (Y/N): ")
csc113Grade  = float(input("CSC 113 grade (0 if not taken): "))
apTestScore  = float(input("CS AP Test Score (0 if not taken): "))

if (haveDiploma == "Y" or haveDiploma == "y" or haveGed == "Y" or haveGed == "y") \
    and (readyForFall == "Y" or readyForFall == "y") \
    and (csc113Grade >= 3.5 or apTestScore >= 4.0):
    print("You've made it!")
else:
    print("Sucks to suck!")
