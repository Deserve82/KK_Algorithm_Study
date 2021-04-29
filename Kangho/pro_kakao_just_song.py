def solution(m, musicinfos):
    answer = ''
    answer_len = 0
    musicinfos.sort()
    tm = []
    for char in m:
        if char != '#':
            tm.append(char)
        else:
            tm[-1] += '#'
    m = tm
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        t = (int(info[1][:2]) - int(info[0][:2])) * 60 + (int(info[1][3:]) - int(info[0][3:]))
        tmp_t = t
        idx, ls = 0, []
        while tmp_t:
            if info[3][idx] != "#":
                ls.append(info[3][idx])
                tmp_t -= 1
                if info[3][(idx+1) % len(info[3])] == "#":
                    ls[-1] += '#'
                    idx += 1
            idx += 1
            idx %= len(info[3])
        for i in range(len(ls)):
            is_same = True
            for j in range(len(m)):
                if not is_same:
                    break
                if i + j < len(ls):
                    if ls[i+j] != m[j]:
                        is_same = False
                else:
                    is_same = False
                    break
            if is_same:
                if answer != '':
                    if answer_len < t:
                        answer = info[2]
                        answer_len = t
                else:
                    answer = info[2]
                    answer_len = t
                break
    if answer == '':
        answer = "(None)"
    return answer
