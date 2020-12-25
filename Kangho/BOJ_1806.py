def subtotal():
    answer = 100000
    tail = 1
    sub_sum = numbers[0]

    for i in range(N):
        while sub_sum < S and tail < N:
            sub_sum += numbers[tail]
            tail += 1
        if sub_sum >= S:
            answer = min(answer, tail - i)
        sub_sum -= numbers[i]
    if answer == 100000:
        answer = 0
    return answer


N, S = map(int, input().split())
numbers = list(map(int, input().split()))
print(subtotal())
