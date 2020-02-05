# 1
sums = []
m = []


def p(t, location):
    if location[0] == len(t)-1:
        m.append(sum(sums))
    else:
        if location[0]+1 < len(t):
            for i in range(2):
                location[0] += 1
                location[1] += i
                sums.append(t[location[0]][location[1]])
                p(t, location)
                location[0] -= 1
                location[1] -= i
                sums.pop()


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
sums.append(triangle[0][0])
answer = 0
p(triangle, [0,0])
print(max(m))


# 2
def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==i:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j],triangle[i-1][j-1])
    return max(triangle[-1])