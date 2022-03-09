def inputAndWriteSchoolData():
    sid  = input("Enter your SID : ")
    name = input("Enter your NAME : ")
    gpa  = input("Enter your GPA : ")

    schoolFile = open("myschooldata2.txt", 'w')
    schoolFile.write(sid  + "\n")
    schoolFile.write(name + "\n")
    schoolFile.write(gpa  + "\n")
    schoolFile.close()

def readAndDisplaySchoolData():
    schoolFile = open("myschooldata.txt", "r")
    sid  = schoolFile.readline().rstrip("\n")
    name = schoolFile.readline().rstrip("\n")
    gpa  = float(schoolFile.readline().rstrip("\n"))
    schoolFile.close()

    print('SID :', sid)
    print('SID :', name)
    print('SID :', format(gpa, '.1f'))
    
def main():
    inputAndWriteSchoolData()
    readAndDisplaySchoolData()

main()
