def dynamic(jarit, last, checker):
    if jarit == N and checker == 1023:
        return 1
    elif jarit == N:
        return 0

    if cache[jarit][last][checker] != -1:
        return cache[jarit][last][checker]

    ret = 0
    if last > 0:
        ret += dynamic(jarit + 1, last-1, checker | (1 << last - 1))
    if last <= 8:
        ret += dynamic(jarit + 1, last+1, checker | (1 << last + 1))
    cache[jarit][last][checker] = ret
    return ret


N = int(input())
cache = [[[-1]*1024 for _ in range(10)] for _ in range(100)]
ans = 0
for i in range(1, 10):
    ans += dynamic(1, i, (1 << i))
print(ans % 1000000000)
