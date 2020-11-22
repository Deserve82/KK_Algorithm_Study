n, m = map(int, input().split())
if m >= 7 and n >= 3:
    print(m-2)
elif n == 2:
    if m <= 2:
        print(1)
    elif m <= 4:
        print(2)
    elif m <= 6:
        print(3)
    else:
        print(4)
else:
    if n >= 3 and m >= 4:
        print(4)
    elif n >= 3 and m >= 3:
        print(3)
    elif n >= 3 and m >= 2:
        print(2)
    else:
        print(1)
