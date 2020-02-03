from itertools import combinations
N, M = map(int, input().split())
bhc_list = []
home_list = []
selected_bhc = []
min_distance = 100000000
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
for home in home_list:
    temp_dis = []
    for stores in selected_bhc:
        for store in stores:
            if home[0] > store[0]:
                temp_r = home[0] - store[0]
            if home[0] <= store[0]:
                temp_r = store[0] - home[0]
            if home[1] > store[1]:
                temp_c = home[1] - store[1]
            if home[1] <= store[1]:
                temp_c = store[1] - home[1]
        temp_dis.append(temp_r+temp_c)
    distance_list.append(min(temp_dis))
    print(distance_list)
if sum(distance_list) < min_distance:
    min_distance = sum(distance_list)

# def bhc_combination(idx):
#     global N
#     global M
#     global min_distance
#     if idx == M:
#         distance_list = []
#         for home in home_list:
#             temp_dis = []
#             for store in selected_bhc:
#                 if home[0] > store[0]:
#                     temp_r = home[0] - store[0]
#                 if home[0] <= store[0]:
#                     temp_r = store[0] - home[0]
#                 if home[1] > store[1]:
#                     temp_c = home[1] - store[1]
#                 if home[1] <= store[1]:
#                     temp_c = store[1] - home[1]
#                 temp_dis.append(temp_r+temp_c)
#             distance_list.append(min(temp_dis))
#         if sum(distance_list) < min_distance:
#             min_distance = sum(distance_list)
#     else:
#         for store in bhc_list:
#             if store not in selected_bhc:
#                 selected_bhc.append(store)
#                 bhc_combination(idx+1)
#                 selected_bhc.pop()
#
#
# bhc_combination(0)
print(min_distance)
