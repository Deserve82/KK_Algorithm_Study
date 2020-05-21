from collections import deque
import sys
l_list = list(sys.stdin.readline().rstrip())
r_list = deque()
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    command = sys.stdin.readline().rstrip()
    if command == 'L' and l_list:
        r_list.appendleft(l_list.pop())
    elif command == 'D' and r_list:
        l_list.append(r_list.popleft())
    elif command == 'B' and l_list:
        l_list.pop()
    else:
        try:
            p, char = command.split()
            l_list.append(char)
        except:
            pass
print("".join(l_list)+"".join(r_list))
