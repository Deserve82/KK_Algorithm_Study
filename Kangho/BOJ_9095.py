test_case = int(input())
dp = [0 for i in range(1000)]


def number_of_case(a):
    if a == 1:
        return 1
    elif a == 2:
        return 2
    elif a == 3:
        return 4
    elif dp[a] != 0:
        return dp[a]
    else:
        for num in range(a-3, a):
            dp[a] += number_of_case(num)
        return dp[a]


for i in range(test_case):
    n = int(input())
    print(number_of_case(n))
