def lcs(x, y):
    lx = len(x)
    ly = len(y)

    check = [[0]*(lx+1) for _ in range(ly+1)]
    for i in range(1, ly+1):
        for j in range(1, lx+1):
            if y[i-1] == x[j-1]:
                check[i][j] += (check[i-1][j-1]+1)
            else:
                check[i][j] = max(check[i-1][j], check[i][j-1])
    return check


a = input()
b = input()
field = lcs(a, b)
you_know_you_are_right = 0
index = field[len(b)][len(a)]

lcs = [""] * (index+1)
lcs[index] = ""

i = len(a)
j = len(b)
while i > 0 and j > 0:

    if a[i-1] == b[j-1]:
        lcs[index-1] = a[i-1]
        i -= 1
        j -= 1
        index -= 1

    elif field[j][i-1] > field[j-1][i]:
        i -= 1
    else:
        j -= 1

print(field[len(b)][len(a)])
print(''.join(lcs))
