n = int(input())
counselling = [0]*100

for i in range(n):
    days, money = map(int, input().split())
    counselling[i+1] = max(counselling[i+1], counselling[i])
    counselling[i+days] = max(counselling[i+days], counselling[i]+money)

print(counselling[n])