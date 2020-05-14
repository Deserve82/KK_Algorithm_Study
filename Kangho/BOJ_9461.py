test_case = int(input())
n = [0] * 1001
n[0] = 0
n[1] = 1
n[2] = 1
n[3] = 1


def dp(k):
    if k == 0:
        return 0
    elif n[k] != 0:
        return n[k]
    else:
        n[k] = dp(k-2) + dp(k-3)
        return n[k]


for i in range(test_case):
    print(dp(int(input())))
