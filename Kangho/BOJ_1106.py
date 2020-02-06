import sys
INF = sys.maxsize
input = sys.stdin.readline

target, N = map(int, input().split())
cities = []
for i in range(N):
    cities.append(list(map(int, input().split())))
dp_list = [INF for i in range(2000)]
dp_list[0] = 0

for i in range(1, 2000):
    temp = []
    for city in cities:
        if i >= city[1]:
            temp.append(min(city[0]+dp_list[i-city[1]], dp_list[i - 1] + city[0]))
        elif i < city[1]:
            temp.append(city[0])
            temp.append(dp_list[i-1]+city[0])
        dp_list[i] = min(temp)

print(min(dp_list[target:]))