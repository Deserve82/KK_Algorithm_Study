from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


testcase = int(input())
for _ in range(testcase):
    a, b = map(int, input().split())
    print(lcm(a, b))
