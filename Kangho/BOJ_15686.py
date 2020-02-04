from itertools import combinations
N, M = map(int, input().split())
bhc_list = []
home_list = []
selected_bhc = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            home_list.append([i, j])
        if temp[j] == 2:
            bhc_list.append([i, j])
            temp[j] = 0
selected_bhc = list(combinations(bhc_list, M))
distance_list = []
for stores in selected_bhc:
    two = []
    for home in home_list:
        one = []
        for store in stores:
            temp_r = abs(home[0]-store[0])
            temp_c = abs(home[1]-store[1])
            one.append(temp_c + temp_r)
        two.append(min(one))
    distance_list.append(sum(two))
print(min(distance_list))