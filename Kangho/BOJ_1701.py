import sys


def get_fail(pat):
    M = len(pat)
    fail = [0] * M
    j = 0
    for i in range(1, M):
        while j > 0 and pat[i] != pat[j]:
            j = fail[j - 1]

        if pat[i] == pat[j]:
            j += 1
            fail[i] = j
        else:
            fail[i] = j
    return max(fail)


txt = sys.stdin.readline()
lt = len(txt)
answer = 0
for i in range(lt):
    answer = max(answer, get_fail(txt[i:]))
print(answer)
