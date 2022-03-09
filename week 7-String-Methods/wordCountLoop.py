def wordStats(phrase):
    wordList = phrase.split(" ")
    
    # determine word count
    wordCount = len(wordList)
    
    # determine average length, shortest word, longest word
    totalLength = 0
    shortestWordLength = 999
    longestWordLength = -999
    for word in wordList:
        wordLen = len(word)
        totalLength += wordLen
        if wordLen < shortestWordLength:
            shortestWordLength = wordLen
        if wordLen > longestWordLength:
            longestWordLength = wordLen
    avgWordLength = totalLength / wordCount
    
    return wordCount, avgWordLength, shortestWordLength, longestWordLength

print(wordStats("see the boy play ball"))
print(wordStats("the antiestablishment candidate handily swept the election"))
