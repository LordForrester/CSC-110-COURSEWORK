studentFile = open("myschooldata3.txt", "r")

studentRecord = studentFile.readline()
# set up while loop, looks for ""
while studentRecord != "":
    studentField = studentRecord.rstrip("\n").split(",")
    studentId     = studentField[0]
    studentName = studentField[1]
    studentGpa = float(studentField[2])
    print(studentId, studentName, studentGpa)
    
    studentRecord = studentFile.readline().strip("\n")
    
studentFile.close()

    
# easier way


studentFile = open("myschooldata3.txt", "r")



for studentRecord in studentFile:
    studentField = studentRecord.rstrip("\n").split(",")
    studentId     = studentField[0]
    studentName = studentField[1]
    studentGpa = float(studentField[2])
    print(studentId, studentName, studentGpa)
    

    
studentFile.close()
