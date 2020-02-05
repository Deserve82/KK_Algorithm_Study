def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    else:
        for word in words:
            count = 0
            for i in range(len(word)):
                if word[i] == begin[i]:
                    pass
                else:
                    count += 1
            if count == 1:
                begin = word
                answer += 1
                temp = 0
                for j in range(len(begin)):
                    if target[j] == begin[j]:
                        pass
                    else:
                        temp += 1
                if temp == 1:
                    answer += 1
                    break
            elif count == 0:
                answer += 1
                break
        return answer