answer = 0
count = 1


def bfs(g):
    global answer
    answer = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                g[i][j] = 0
                g[j][i] = 0
                que = [j]
                answer += 1
                while que:
                    haha = que.pop(0)
                    for k in range(n):
                        if g[haha][k] == 1:
                            que.append(k)
                            g[haha][k] = 0
                            g[k][haha] = 0


while True:
    n = int(input())
    if n == 0:
        break
    graph = [[0] * n for _ in range(n)]
    people = []
    for _ in range(n):
        f1 = False
        f2 = False
        name1, name2 = input().split()
        if name1 not in people:
            people.append(name1)
            f1 = True
        if name2 not in people:
            people.append(name2)
            f2 = True

        if f1 and f2:
            graph[len(people) - 1][len(people) - 2] = 1
            graph[len(people) - 2][len(people) - 1] = 1
        else:
            index1 = 0
            index2 = 0
            for i in range(len(people)):
                if people[i] == name1:
                    index1 = i
                if people[i] == name2:
                    index2 = i
            graph[index1][index2] = 1
            graph[index2][index1] = 1
    bfs(graph)
    print(count, answer)
    count += 1 
