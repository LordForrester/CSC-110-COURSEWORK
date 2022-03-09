studentLine = "123432,John Jones,29,350.78"
studentFields = studentLine.split(",")
print(len(studentFields))

for studField in studentFields:
    print(studField)

studId = studentFields[0]
studName = studentFields[1]
studAge = int(studentFields[2])
studBal = float(studentFields[3])

print(studId, studName, studAge, studBal)
