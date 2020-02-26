n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))

dps = [0]*400

def dp(idx):
    global n
    if idx == 1:
        dps[1] = stairs[1]
        return dps[1]
    elif idx == 2:
        dps[2] = stairs[1]+stairs[2]
        return dps[2]
    elif idx == 3:
        dps[3] = max(stairs[3]+stairs[1], stairs[3]+stairs[2])
        return dps[3]
    elif dps[idx] != 0:
        return dps[idx]
    else:
        dps[idx] = max(dp(idx-2)+stairs[idx], dp(idx-3)+stairs[idx]+stairs[idx-1])
        return dps[idx]

print(dp(n))