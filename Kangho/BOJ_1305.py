def get_fail(pat):
    M = len(pat)
    fail = [0] * M
    j = 0
    for i in range(1, M):
        while j > 0 and pat[i] != pat[j]:
            j = fail[j-1]

        if pat[i] == pat[j]:
            j += 1
            fail[i] = j
        else:
            fail[i] = j
    return fail


N = int(input())
txt = input()
print(N - get_fail(txt)[-1])
