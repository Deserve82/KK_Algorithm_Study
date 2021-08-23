import heapq as hq


def get_length(a, b):
    return (abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2) ** 0.5


def get_parent(a):
    if parents[a] == a:
        return a
    parents[a] = get_parent(parents[a])
    return parents[a]


def merge(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if a == b:
        return
    parents[b] = a


n = int(input())
q = []
parents = [i for i in range(n)]
spots = []
board = [[0]*n for _ in range(n)]
for _ in range(n):
    x, y = map(float, input().split())
    spots.append([x, y])

for i in range(n):
    for j in range(i+1, n):
        l = get_length(spots[i], spots[j])
        hq.heappush(q, [l, i, j])

answer = 0
while q:
    l, f, t = hq.heappop(q)
    if get_parent(f) != get_parent(t):
        answer += l
        merge(f, t)
print("{:.2f}".format(answer))
