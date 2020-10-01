def decompresss(s, ind):
    let = s[ind]
    if let == 'w' or let == 'b':
        return let

    ind += 1
    a = decompresss(s, ind)
    ind += len(a)
    b = decompresss(s, ind)
    ind += len(b)
    c = decompresss(s, ind)
    ind += len(c)
    d = decompresss(s, ind)
    return 'x' + c + d + a + b


n = int(input())
for _ in range(n):
    sen = input()
    print(decompresss(sen, 0))
