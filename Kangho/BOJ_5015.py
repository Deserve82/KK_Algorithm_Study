from sys import stdin


def wild(pattern_idx, compare_idx):
    if cache[pattern_idx][compare_idx] != -1:
        return cache[pattern_idx][compare_idx]

    if pattern_idx < pattern_len and compare_idx < compare_len and \
            compare_string[compare_idx] == pattern_string[pattern_idx]:
        cache[pattern_idx][compare_idx] = wild(pattern_idx + 1, compare_idx + 1)
        return cache[pattern_idx][compare_idx]

    if pattern_idx == pattern_len:
        cache[pattern_idx][compare_idx] = int(compare_idx == compare_len)
        return cache[pattern_idx][compare_idx]

    if pattern_string[pattern_idx] == '*':
        if wild(pattern_idx + 1, compare_idx) or (compare_idx < compare_len and wild(pattern_idx, compare_idx + 1)):
            cache[pattern_idx][compare_idx] = 1
            return cache[pattern_idx][compare_idx]

    cache[pattern_idx][compare_idx] = 0
    return cache[pattern_idx][compare_idx]


pattern_string = input()
strings = []
a = int(stdin.readline())
for _ in range(a):
    strings.append(stdin.readline())
for compare_string in strings:
    pattern_len = len(pattern_string)
    compare_len = len(compare_string)
    cache = [[-1] * (compare_len + 1) for _ in range(pattern_len + 1)]
    if wild(0, 0):
        print(compare_string)
