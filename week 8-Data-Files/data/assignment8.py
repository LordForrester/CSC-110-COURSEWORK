def main():
    #askes for data and validates input
    userRiver = input("Which river? ")
    while userRiver == "":
        userRiver = input("Which river? ")
    userMonth = int(input("Which month? (e.g., 1 for January)? "))
    
    while userMonth     < 1 or userMonth > 12:
        userMonth       = int(input("Which month? "))
    print()
    userPollutant       = int(input("Available pollutants: "))
    
    while userPollutant < 1 or userPollutant > 4:
        userPollutant   = int(input("Available pollutants: "))
        
    # opens data file and reads 1 line to be properally positioned for looping
    file = open("rivers.txt")
    file.readline()
    
    lowestRead  = 10000
    highestRead = -99
    rowCount    = 0
    readSum     = 0
    #seperates data by ",", on every line of file
    # and stores data perline on seperate variables
    for line in file:
        riverField         = line.rstrip("\n").split(",")
        riverName          = riverField[0]
        riverMonth         = int(riverField[1])
        riverArsenic       = riverField[3]
        riverLead          = riverField[4]
        riverFertilizer    = riverField[5]
        riverPesticide     = riverField[6]

        # creates a variables with the name of the pollution chosen by the user
        if userPollutant   == 1:
            listPollutant  = int(riverArsenic)
            dataPollutant  = "Arsenic"
                
        elif userPollutant == 2:
            listPollutant  = int(riverLead)
            dataPollutant  = "Lead"    
        elif userPollutant == 3:
            listPollutant  = float(riverFertilizer)
            dataPollutant  = "Fertilizer"    
        else:
            listPollutant  = float(riverPesticide)
            dataPollutant  = "Pesticide "
        if userRiver == riverName and riverMonth == userMonth:

            
            rowCount+= 1
            readSum+= listPollutant  
             
            if listPollutant   > highestRead:
                highestRead    = listPollutant
                
            if listPollutant   < lowestRead:
                lowestRead     = listPollutant
                
    file.close()
    readAverage = round(readSum / rowCount, 3)

    #convert back into strings
    print()
    print("Processing of", rowCount, "rows is complete.  See summary file for results.")
    userMonth = str(userMonth)
    rowCount = str(rowCount)
    readAverage = str(readAverage)
    lowestRead = str(lowestRead)
    highestRead = str(highestRead)
    
    # format into file
    summaryFile = open("PollutionSummary.txt", "a")
    summaryFile.write("Data for river: " + userRiver + "\n")
    summaryFile.write("Data for month: " + userMonth + "\n")
    summaryFile.write("Data for pollutant:  " + dataPollutant + "\n\n")
   
    summaryFile.write("Data for readings:  "     + rowCount    + "\n")
    summaryFile.write("Average of readings:    " + readAverage + "\n")
    summaryFile.write("Lowest reading:         " + lowestRead  + "\n")
    summaryFile.write("Highest reading:        " + highestRead + "\n\n")
    print(("Number of readings \t" + rowCount))             
                       
main()

#Test 1: input: Brazos River, 2, 4
#   able to loop through desired lines in file, but unable to correctly store highestRead.
#   Value remains at -99.
#Test 2: After changing the order of the loop, result is now 0.0, better but not correct.
#   i eventually realize that I need to convert the data values into int and float values INSIDE the loop, not before.

#Test 3: output for highestRead is correct, finished the rest of the output,
#   all correct, but \t was not working inside the file

#Test 4: I decide to use spaces instead, output is correct.



#Summary
# I began the assignment by figuring out how many variables I was going to need
# After creating the variables, I moved on to opening and reading the river file in a for loop
# I seperated the data in the file by "," and assigned each string to a variable
#I got stuck after doing this, because I did not convert riverMonth to an integer
#After writing the loop, I convert the varaibles back into strings to be written into PollutionSummary.txt
# I was uanble to use \t when formatting the strings inside the file, so I just used spaces


    
