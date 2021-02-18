import sys
input = sys.stdin.readline
for _ in range(int(input())):
    h = input()
    f = input()

    hyper = 0
    for i, char in enumerate(h):
        if char == "M":
            hyper |= (1 << i)
    fans = 0
    for i, char in enumerate(f):
        if char == "M":
            fans |= (1 << i)
    gap = len(f) - len(h)
    answer = 0
    for i in range(gap+1):
        if hyper & fans != 0:
            pass
        else:
            answer += 1
        fans = fans >> 1
    print(answer)
