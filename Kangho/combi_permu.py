def permu():
    if len(val) > m:
        return
    if len(val) == m:
        print(val)
    for i in range(len(arr)):
        if not check[i]:
            check[i] = True
            val.append(arr[i])
            permu()
            val.pop()
            check[i] = False


def combi(idx):
    if len(val) > m:
        return
    if len(val) == m:
        print(val)
    for i in range(idx, len(arr)):
        if not check[i]:
            check[i] = True
            val.append(arr[i])
            combi(i + 1)
            val.pop()
            check[i] = False


n, m = map(int, input().split())
check = [False] * n
val = []
arr = [i for i in range(1, n + 1)]
permu()
print("-----------------")
combi(0)
