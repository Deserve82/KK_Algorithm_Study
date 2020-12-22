MOD = 1000000007
def tiling(idx):
    if idx == 1:
        return 1
    elif idx == 2:
        return 2
    elif cache[idx] != -1:
        return cache[idx]

    cache[idx] = tiling(idx - 1) + tiling(idx - 2)
    return cache[idx]


def atile(w):
    if w <= 2:
        return 0
    if w % 2 == 1:
        return (tiling(w) - tiling(int(w/2)) + MOD) % MOD
    ret = tiling(w)
    ret = (ret - tiling(int(w/2)) + MOD) % MOD
    ret = (ret - tiling(int(w/2)-1) + MOD) % MOD
    return ret


for _ in range(int(input())):
    cache = [-1] * 101
    cache[1], cache[2] = 1, 2
    i = int(input())
    tiling(i)
    print(atile(i))
    
# 종만북 풀이..
