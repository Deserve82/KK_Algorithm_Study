import sys


def catch_me_if_you_can(loc, day):
    if day == days:
        if loc == q:
            return 1
        return 0

    if cache[loc][day] != -1:
        return cache[loc][day]

    cache[loc][day] = 0
    for i in range(vils):
        if board[loc][i] == 1:
            cache[loc][day] += (catch_me_if_you_can(i, day + 1) / connected_to_vil[loc])
    return cache[loc][day]


if __name__ == '__main__':
    for _ in range(int(sys.stdin.readline())):
        vils, days, pri_vil = map(int, sys.stdin.readline().split())
        board = []
        for _ in range(vils):
            board.append(list(map(int, sys.stdin.readline().split())))
        pos_vil = int(input())
        possible_villages = list(map(int, sys.stdin.readline().split()))

        connected_to_vil = [1] * vils
        for k in range(vils):
            cnt = 0
            for j in range(vils):
                if board[k][j] == 1:
                    cnt += 1
            connected_to_vil[k] = cnt
        answer = ''
        for q in possible_villages:
            cache = [[-1] * 101 for _ in range(51)]
            answer += str(round((catch_me_if_you_can(pri_vil, 0)), 8)) + " "
        print(answer)
