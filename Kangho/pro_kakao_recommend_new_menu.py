def solution(orders, course):
    answer = set()
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    point = {}
    for i, char in enumerate(alph):
        point[char] = i
    what_we_have = {}
    mv = {}
    for c in course:
        mv[c] = 0
        what_we_have[c] = []
    bit_orders = []
    for order in orders:
        person = 0
        for char in order:
            person |= (1 << point[char])
        bit_orders.append(person)
    for i, bit_order in enumerate(bit_orders):
        for j, oth_order in enumerate(bit_orders):
            if i <= j:
                continue
            else:
                num = bit_order & oth_order
                ori_num = num
                num_lis = []
                while num:
                    num_lis.append(num)
                    num = (num-1) & ori_num
                for num in num_lis:
                    num_same_things = bin(num).count("1")
                    if num_same_things in course:
                        answer.add((num, num_same_things))
    for ans in answer:
        cnt = 0
        for bit_order in bit_orders:
            if bit_order & ans[0] == ans[0]:
                cnt += 1
        what_we_have[ans[1]].append((cnt, ans[0]))
        if mv[ans[1]] < cnt:
            mv[ans[1]] = cnt
    real_answer = []
    for k, v in what_we_have.items():
        for ccnt, val in v:
            if ccnt == mv[k]:
                real_answer.append(bin(val))
    tmp_ans = []
    for ans in real_answer:
        ans = ans[::-1]
        tmp = ''
        for a, dd in zip(ans, alph):
            if a == '1':
                tmp += dd
        tmp_ans.append(tmp)
    tmp_ans.sort()
    return tmp_ans
