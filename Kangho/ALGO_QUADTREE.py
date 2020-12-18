# 종만북 방법
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


# 내가 푼 방법
def quad(idx):
    global sl, string
    quads = ['', '', '', '']
    quad_idx = 0
    while idx < sl and quad_idx < 4:
        if string[idx] == 'x':
            temp = quad(idx+1)
            quads[quad_idx] = 'x' + temp
            idx += len(quads[quad_idx])
            quad_idx += 1
        else:
            quads[quad_idx] = string[idx]
            quad_idx += 1
            idx += 1

    return quads[2] + quads[3] + quads[0] + quads[1]


if __name__ == '__main__':
    n = int(input())
    string = ''
    for _ in range(n):
        string = input()
        sl = len(string)
        print(quad(0))
