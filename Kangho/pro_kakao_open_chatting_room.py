def solution(record):
    answer = []
    tmp = []
    user = {}
    for one in record:
        one = one.split(" ")
        if one[0] == 'Enter':
            user[one[1]] = one[2]
            tmp.append((one[0], one[1]))
        elif one[0] == "Leave":
            tmp.append((one[0], one[1]))
        else:
            user[one[1]] = one[2]
    for i in tmp:
        if i[0] == "Enter":
            answer.append(user[i[1]]+"님이 들어왔습니다")
        else:
            answer.append(user[i[1]]+"님이 나갔습니다")
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))