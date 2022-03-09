file = open("lab08numbers.txt", 'r')
evenSum  = 0
oddCount = 0
for number in file:
    
    print(number.strip("\n"))
    number = int(number)
    
    if number %2 == 0:
        evenFile = open("even.txt", "a")
        evenFile.write(str(number)+ "\n")
        evenFile.close()
        evenSum = evenSum + number
    else:
        oddFile = open("odd.txt", "a")
        oddFile.write(str(number)+ "\n")
        oddFile.close()
        oddCount+= 1
print(evenSum)
print(oddCount)
        
        
    
file.close()


    


