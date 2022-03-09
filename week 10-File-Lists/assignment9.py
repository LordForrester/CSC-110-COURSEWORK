#wordLenFreqs = [0, 0, 0, 0, 0, 0]

#if you see the world 'the'

#wordLenFreqs[3] += 1

#print(wordLenFreqs)


def readFile(fileName):
    wordFile = open(fileName, "r")
    distinctWords = []
    for line in wordFile:
        lineList = line.split()
    lineList = set(lineList)
    return lineList
        
def findLongest(setOfWords):
    longestWord = ""
    
    for word in setOfWords:
        if len(word) > len(longestWord):
            longestWord = word
    lengthOfWord = len(longestWord)
    return longestWord, lengthOfWord

def generateSortedList(setOfWords):
    return sorted(setOfWords)
    
        
def main():    

    print(readFile("wordFile.txt"))

    print(findLongest({'hi', 'the', 'where'}))

    print(generateSortedList({'hi', 'the', 'where'}))

main()
