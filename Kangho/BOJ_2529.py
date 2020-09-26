from itertools import permutations

ls = [i for i in range(10)]
n = int(input())
bd = input().split(' ')
bd.append('')

max_ls = ls[9 - n:]
max_check = [False] * (n + 1)
min_ls = ls[:n + 1]

max_v = ''
answer_list = []


def check(ls, c, s):
    global max_v
    if c == n + 1:
        answer_list.append(max_v)
    for i in range(n + 1):
        if not max_check[i]:
            if max_v == '':
                max_v += str(ls[i])
                max_check[i] = True
                check(ls, c + 1, bd[c])
                max_check[i] = False
                max_v = max_v[:-1]
            elif s == '>':
                if int(max_v[-1]) > ls[i]:
                    max_v += str(ls[i])
                    max_check[i] = True
                    check(ls, c + 1, bd[c])
                    max_check[i] = False
                    max_v = max_v[:-1]
            else:
                if int(max_v[-1]) < ls[i]:
                    max_v += str(ls[i])
                    max_check[i] = True
                    check(ls, c + 1, bd[c])
                    max_check[i] = False
                    max_v = max_v[:-1]


check(max_ls, 0, '')
check(min_ls, 0, '')
print(max(answer_list))
print(min(answer_list))
