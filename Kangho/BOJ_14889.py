from itertools import combinations


# 팀 나누는 함수 겹치지 않게 딱 둘로 나누어 준다
def divideTeam(arr):
    teamList = []
    checkList = list(combinations(arr, int(len(arr)/2)))
    for i in checkList:
        team_f = []
        team_s = []
        for j in i:
            if i not in arr:
                team_f.append(j)
        for i in arr:
            if i not in team_f:
                team_s.append(i)
        teamList.append([team_f, team_s])
    return teamList[0:int(len(teamList)/2)]


# 팀별로 하나씩 최소 값을 찾은 리스트 중 최솟 값을 반환하는 것
def gap(numberOfCombinations):
    gapList = []
    for game in numberOfCombinations:
        firstTeamPoint = 0
        firstTeam = list(combinations(game[0], 2))
        for point in firstTeam:
            firstTeamPoint += field[point[0]][point[1]] + field[point[1]][point[0]]
        secondTeamPoint = 0
        secondTeam = list(combinations(game[1], 2))
        for point in secondTeam:
            secondTeamPoint += field[point[0]][point[1]] + field[point[1]][point[0]]
        if firstTeamPoint >= secondTeamPoint:
            gapList.append(firstTeamPoint - secondTeamPoint)
        else:
            gapList.append(secondTeamPoint - firstTeamPoint)
    return min(gapList)


# 입력 받기
N = int(input())
field = []
for i in range(N):
    field.append(list(map(int, input().split())))
tempField = [num for num in range(0, N)]

numberOfCombinations = divideTeam(tempField)
print(gap(numberOfCombinations))