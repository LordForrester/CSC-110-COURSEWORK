CHARS_PER_LINE = 80
COLS_DESIRED = 4
WORD_FMT = str(CHARS_PER_LINE // COLS_DESIRED) + "s"

moonFile = open("GoodnightMoon.txt", "r")
vocabSet = set()
for word in moonFile:
    vocabSet.add(word.strip())
moonFile.close()

vocabList = list(vocabSet)
vocabList.sort()

for vocabIdx in range(0, len(vocabList)):
    print(format(vocabList[vocabIdx], WORD_FMT), end = "")
    if vocabIdx % COLS_DESIRED == COLS_DESIRED - 1: 
        print()
