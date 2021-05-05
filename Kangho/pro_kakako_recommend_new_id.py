def solution(new_id):
    valid = 'abcdefghijklmnopqrstuvwxyz.-_0123456789'
    answer = ''
    # 1
    new_id = new_id.lower()

    # 2
    tmp = ''
    for char in new_id:
        if char in valid:
            tmp += char
    new_id = tmp

    point_cnt = 0
    tmp = ''
    for char in new_id:
        if char == '.':
            point_cnt += 1
        else:
            if point_cnt >= 1:
                tmp += '.'
            point_cnt = 0
            tmp += char
    new_id = tmp
    if new_id:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if not new_id:
        new_id = 'a'

    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    while len(new_id) < 3:
        new_id += new_id[-1]
    answer = new_id
    return answer
