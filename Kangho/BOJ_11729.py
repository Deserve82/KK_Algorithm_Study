import sys, math
sys.setrecursionlimit(1000000)


def hanoi(n, from_num, by_num, to_num):
    if n < 21:
        if n == 1:
            print(from_num, to_num)
            return
        else:
            hanoi(n - 1, from_num, to_num, by_num)
            print(from_num, to_num)
            hanoi(n - 1, by_num, from_num, to_num)


m = int(sys.stdin.readline())
print(int(math.pow(2, m))-1)
hanoi(m, 1, 2, 3)
