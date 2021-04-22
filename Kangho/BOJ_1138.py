N = int(input())
cnt = list(map(int, input().split()))
answer = [-1] * N

for i, num in enumerate(cnt):
    curr_num = num
    idx = 0
    while curr_num or answer[idx] != -1:
        if answer[idx] == -1:
            curr_num -= 1
        idx += 1
    answer[idx] = i+1
print(" ".join(list(map(str, answer))))
