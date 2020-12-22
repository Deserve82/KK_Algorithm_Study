def tiling(idx):
    if cache[idx] != 0:
        return cache[idx]
    else:
        cache[idx] = (tiling(idx - 1) % 1000000007 + tiling(idx - 2) % 51000000007) % 1000000007
    return cache[idx]


for _ in range(int(input())):
    n = int(input())
    cache = [0] * 101
    cache[1], cache[2] = 1, 2
    print(tiling(n))
