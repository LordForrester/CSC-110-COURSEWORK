#custFile = open("myDataFile.txt", "r")
#custCount = int(custFile.readline().strip())

#for cust in range(0, custCount):
#    custName = custFile.readline().strip()
#    custAge = int(custFile.readline().strip())
#    custBalance = float(custFile.readline().strip())
#    print(custName, custAge, custBalance)

#custFile.close()

# now lets write something to WRITE INTO myDataFile.txt, or something like it


#when we use "w" here, we are saying "if the file doesnt exist, create it and write into it.
#   if file did exist, this would just write into it.
custFile = open("myDataFile.txt", "w")
custName = "Morgan Manchester"
custAge = 27
custBalance = 1234.93

custFile.write(custName + "\n")
#trying to write integers will cause an error, so convert them to strings
custFile.write(str(custAge)+ "\n")
custFile.write(str(custBalance)+ "\n")
 
custFile.close()

print("Data was writtien to the file MyDataFile.txt")
