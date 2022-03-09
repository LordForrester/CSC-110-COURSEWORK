def inputAndWriteSchoolData():
    sid  = input("Enter your SID : ")
    name = input("Enter your NAME : ")
    gpa  = input("Enter your GPA : ")

    schoolFile = open("myschooldata.txt", 'w')
    schoolFile.write(sid  + "\n")
    schoolFile.write(name + "\n")
    schoolFile.write(gpa  + "\n")
    schoolFile.close()

    
def main():
    inputAndWriteSchoolData()

main()
