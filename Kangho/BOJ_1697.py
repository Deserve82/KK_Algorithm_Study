from collections import deque
sp, ep = map(int, input().split())
check = [False] * 100001
loc = deque()
loc.append((sp, 0))
check[sp] = True
while loc:
    cl, counter = loc.popleft()
    if cl == ep:
        print(counter)
        break
    else:
        counter += 1
        if cl - 1 >= 0:
            if not check[cl-1]:
                check[cl-1] = True
                loc.append((cl-1, counter))
        if cl + 1 < 100001:
            if not check[cl+1]:
                check[cl+1] = True
                loc.append((cl+1, counter))
        if cl * 2 < 100001:
            if not check[cl*2]:
                check[cl*2] = True
                loc.append((cl*2, counter))
