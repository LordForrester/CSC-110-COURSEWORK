#input
studentName = input("Enter your name: ")
studentId = input("Enter your student ID nuimber: ")

math142Date = input("\nWhen did you take MATH142?")
math142Grade = float(input("Enter your grade for MATH142: "))

csc110Date = input("\nWhen did you take CSC110?")
csc110Grade = float(input("Enter your grade for CSC110: "))

csc142Date = input("\nWhen did you take CSC142?")
csc142Grade = float(input("Enter your grade for CSC142: "))


csc143Date = input("\nWhen did you take CSC143?")
csc143Grade = float(input("Enter your grade for CSC143: "))

#output

print("\nStudent name:", studentName)
print("ID number:", studentId)

print("\n- - > G r a d e  R e p o r t < - -")

print("\nCourse\tDescription\t\t\tGrade\t\tTaken")
print("------\t--------------------\t\t-----\t\t---------------")
print("MATH142\t" "Precalculus\t", math142Grade, math142Date, sep = "\t\t")
print("CSC110\t" "Intro to Pgm.\t", csc110Grade, csc110Date, sep = "\t\t")
print("CSC142\t" "Computer Pgm. I\t", csc142Grade, csc142Date, sep = "\t\t")
print("CSC143\t" "Computer Pgm. II", csc143Grade, csc143Date, sep = "\t\t")




#first test: the alignment for CSC143 data was off by a couple tabs.
#second test: after adding extra tabs to the course descriptions, I was able to
#line everything correctly
#I struggled with formatting the alignment correctly because of extra tabs being forced due to a long string
# I tested the program by inputing answers to see if the input would line up correctly
# I learned how string length can effect the way alignment works, as well as how to use tabs correctly
