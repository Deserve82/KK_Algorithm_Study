N = int(input())
for i in range(N):
    aNumber, theNumber = map(int, input().split())
    importanceList = list(map(int, input().split()))
    answer = 0
    while theNumber >= 0:
        firstPopFlag = 0
        for c in range(len(importanceList)):
            if importanceList[0] < importanceList[c]:
                temp = importanceList.pop(0)
                importanceList.append(temp)
                theNumber -= 1
                if theNumber < 0:
                    theNumber = len(importanceList)-1
                break
            if c == len(importanceList)-1:
                firstPopFlag = 1
        if firstPopFlag == 1:
            importanceList.pop(0)
            theNumber -= 1
            answer += 1

    print(answer)