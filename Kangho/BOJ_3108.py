from collections import deque
def dfs(idx):
    stack = [squares[idx]]
    while stack:
        left_down, right_up = stack.pop()
        for i in range(N):
            if not check[i]:
                cld, cru = squares[i]
                completely_covered = False
                is_separated = False

                if (right_up[0] < cld[0] or right_up[1] < cld[1]) or (cru[0] < left_down[0] or cru[1] < left_down[1]):
                    is_separated = True

                if right_up[0] > cru[0] and right_up[1] > cru[1] and left_down[0] < cld[0] and left_down[1] < cld[1]:
                    completely_covered = True

                if right_up[0] < cru[0] and right_up[1] < cru[1] and left_down[0] > cld[0] and left_down[1] > cld[1]:
                    completely_covered = True

                if not completely_covered and not is_separated:
                    check[i] = True
                    stack.append(squares[i])
                else:
                    continue


N = int(input())
check = [False] * N
squares = deque()
ans = 0
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 == 0 and y2 >= 0 and y1 <= 0) or (x2 == 0 and y1 <= 0 and y2 >= 0) or (y1 == 0 and x2 >= 0 and x1 <= 0) or\
            (y2 == 0 and x1 <= 0 and x2 >= 0):
        squares.appendleft([(x1, y1), (x2, y2)])
    else:
        squares.append([(x1, y1), (x2, y2)])

for i in range(N):
    x1, y1 = squares[i][0]
    x2, y2 = squares[i][1]
    if (x1 == 0 and y2 >= 0 and y1 <= 0) or (x2 == 0 and y1 <= 0 and y2 >= 0) or (y1 == 0 and x2 >= 0 and x1 <= 0) or\
            (y2 == 0 and x1 <= 0 and x2 >= 0):
        check[i] = True
        dfs(i)
    elif not check[i]:
        check[i] = True
        ans += 1
        dfs(i)
print(ans)
