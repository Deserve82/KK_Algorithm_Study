def solution(new_id):
    new_id = new_id.lower() # 1단계
    special_letters = "~!@#$%^&*()=+[{]}:?,<>"
    l = len(new_id)
    new_list = list(new_id)
    i = 0
    while i < l: # 2단계
        if new_list[i] in special_letters:
            new_list.pop(i)
            l -= 1
        else:
            i += 1
    nl = len(new_list)
    if new_list and nl > 2: # 3단
        prev = new_list[0]
        j = 1
        while j < nl:
            if prev == '.' and new_list[j] == '.':
                new_list.pop(j)
                nl -= 1
            else:
                prev = new_list[j]
                j += 1
    while new_list and len(new_list) > 0:
        if new_list[0] == '.':
            new_list.pop(0)
        elif new_list[-1] == '.':
            new_list.pop()
        else:
            break
    nl = len(new_list)
    if nl == 0:
        new_list = ['a']
    nnl = len(new_list)
    if nnl > 15:
        while nnl > 15:
            new_list.pop()
            nnl -= 1
    while new_list[-1] == '.':
        new_list.pop()
        if not new_list: break
    if nl == 0:
        new_list = ['a']
    if nnl < 3:
        while nnl < 3:
            new_list.append(new_list[-1])
            nnl += 1
    answer = "".join(new_list)
    return answer

print(solution("__._.."))

