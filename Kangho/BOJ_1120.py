a, b = input().split(" ")
gap = len(b)-len(a)
min_dif = 1000
for i in range(gap+1):
    dif = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            dif += 1
    if dif < min_dif:
        min_dif = dif

print(min_dif)
