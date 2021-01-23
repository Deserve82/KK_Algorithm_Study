from collections import deque
import bisect


def remove_dominated():
    global length, answer, ps, ra, bigger_idx
    people.insert(bigger_idx, (ps, ra))
    while bigger_idx > 0:
        bigger_idx -= 1
        if people[bigger_idx][0] < ps and people[bigger_idx][1] < ra:
            length -= 1
            del people[bigger_idx]
        else:
            break
    length += 1
    answer += length


for _ in range(int(input())):
    N = int(input())
    people = deque()
    answer = 0
    length = 0
    for _ in range(N):
        ps, ra = map(int, input().split())
        if people:
            bigger_idx = bisect.bisect_right(people, (ps, ra))
            if bigger_idx == 0:
                if people[0][0] > ps and people[0][1] > ra:
                    answer += length
                    continue
                else:
                    people.appendleft((ps, ra))
                    length += 1
                    answer += length
            else:
                remove_dominated()
        else:
            length += 1
            answer += length
            people.append((ps, ra))
    print(answer)
