def facto(num):
    if num == 1:
        return 1
    return num * facto(num-1)

def solution(n, k):
    answer = []
    numbers = [i for i in range(1, n+1)]
    while n > 0:
        val = facto(n)
        pivot_index = val // n
        idx = 0
        while k > pivot_index:
            k -= pivot_index
            idx += 1
        answer.append(numbers[idx])
        numbers.remove(numbers[idx])
        n -= 1
    return answer
