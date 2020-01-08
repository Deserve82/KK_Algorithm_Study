N = int(input())
for i in range(N):
    aNumber, theNumber = map(int, input().split())
    importanceList = list(map(int, input().split()))

answer = 0
while theNumber:
    for c in range(len(importanceList)):
        if theNumber < 0:
            break
        if importanceList[0] < importanceList[c]:
            if c == theNumber:
                theNumber = len(importanceList)-1
            temp = importanceList.pop(0)
            importanceList.append(temp)
            theNumber -= 1
        else:
            importanceList.pop(0)
            theNumber -= 1
            answer += 1

print(answer)