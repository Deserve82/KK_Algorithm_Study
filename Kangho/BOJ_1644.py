def primes_up_to(n: int) -> [int]:
    seive = [False, False] + [True] * (n-1)
    for (i, e) in enumerate(seive):
        if e:
            k = i * 2
            while k <= n:
                seive[k] = False
                k += i
    return [x for (x, y) in enumerate(seive) if y]


N = int(input())
primes = primes_up_to(N)
lp = len(primes)
left = 0
right = 1
cnt = 0
if N != 1:
    sum_of_total = primes[0]
    while left < right <= lp:
        if sum_of_total == N:
            cnt += 1
            if right < lp:
                sum_of_total += primes[right]
                right += 1
            else:
                sum_of_total -= primes[left]
                left += 1
        elif sum_of_total < N and right < lp:
            sum_of_total += primes[right]
            right += 1
        else:
            sum_of_total -= primes[left]
            left += 1
print(cnt)
