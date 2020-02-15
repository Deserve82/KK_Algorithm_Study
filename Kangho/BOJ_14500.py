n, m = map(int, input().split())
f = []
for _ in range(n):
    f.append(list(map(int, input().split())))

max_v = 0
for i in range(n):
    for j in range(m):
        if i <= n-2 and j <= m-2:
            square = f[i][j] + f[i + 1][j] + f[i][j + 1] + f[i + 1][j + 1]
            if max_v < square:
                max_v = square
        if j < m-3:
            c_stick = f[i][j] + f[i][j+1] + f[i][j+2] + f[i][j+3]
            if max_v < c_stick:
                max_v = c_stick
        if i < n-3:
            r_stick = f[i][j] + f[i+1][j] + f[i+2][j] + f[i+3][j]
            if max_v < r_stick:
                max_v = r_stick
        if i <= n-3 and j < m-1:
            hook_1 = f[i][j] + f[i+1][j] + f[i+2][j] + f[i+2][j+1]
            if max_v < hook_1:
                max_v = hook_1
        if i <= n-3 and 0 < j < m:
            hook_2 = f[i][j] + f[i+1][j] + f[i+2][j] + f[i+2][j-1]
            if max_v < hook_2:
                max_v = hook_2
        if i < n-1 and j < m-2:
            hook_3 = f[i][j] + f[i][j+1] + f[i][j+2] + f[i+1][j+2]
            if max_v < hook_3:
                max_v = hook_3
        if i < n-1 and 1 < j:
            hook_4 = f[i][j] + f[i][j-1] + f[i][j-2] + f[i+1][j-2]
            if max_v < hook_4:
                max_v = hook_4
        if i < n-2 and j < m-1:
            hook_5 = f[i][j] + f[i][j+1] + f[i+1][j+1] + f[i+2][j+1]
            if max_v < hook_5:
                max_v = hook_5
        if i < n-2 and 0 < j:
            hook_6 = f[i][j] + f[i][j-1] + f[i+1][j-1] + f[i+2][j-1]
            if max_v < hook_6:
                max_v = hook_6
        if i < n-1 and j < m-2:
            hook_7 = f[i][j] + f[i+1][j] + f[i+1][j+1] + f[i+1][j+2]
            if max_v < hook_7:
                max_v = hook_7
        if i < n-1 and 1 < j:
            hook_8 = f[i][j] + f[i+1][j] + f[i+1][j-1] + f[i+1][j-2]
            if max_v < hook_8:
                max_v = hook_8
        if i <= n-2 and j+2 < m:
            z1 = f[i][j] + f[i][j+1] + f[i+1][j+1] + f[i+1][j+2]
            if max_v < z1:
                max_v = z1
        if i < n-2 and j+1 < m:
            z2 = f[i][j] + f[i+1][j] + f[i+1][j+1] + f[i+2][j+1]
            if max_v < z2:
                max_v = z2
        if i < n-2 and 0 < j < m:
            z3 = f[i][j] + f[i+1][j] + f[i+1][j-1] + f[i+2][j-1]
            if max_v < z3:
                max_v = z3
        if i <= n-2 and 1 < j < m:
            z4 = f[i][j] + f[i][j-1] + f[i+1][j-1] + f[i+1][j-2]
            if max_v < z4:
                max_v = z4
        if i < n-1 and j < m-2:
            f1 = f[i][j] + f[i][j+1] + f[i][j+2] + f[i+1][j+1]
            if max_v < f1:
                max_v = f1
        if i < n-2 and j < m-1:
            f2 = f[i][j] + f[i+1][j] + f[i+2][j] + f[i+1][j+1]
            if max_v < f2:
                max_v = f2
        if 0 < i < n and j < m-2:
            f3 = f[i][j] + f[i][j+1] + f[i][j+2] + f[i-1][j+1]
            if max_v < f3:
                max_v = f3
        if 0 < i < n-1 and 0 < j < m-1:
            f4 = f[i][j] + f[i-1][j+1] + f[i][j+1] + f[i+1][j+1]
            if max_v < f4:
                max_v = f4
print(max_v)
