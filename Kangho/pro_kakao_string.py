def solution(s):
    answer = len(s)
    for word in range(1, int(len(s)/2)+1):
        count = 0
        temp_word = s[word:]
        temp_pivot = s[0:word]
        temp_word_count = 1
        while True:
            if temp_pivot == temp_word[:word] and word <= len(temp_word):
                temp_word = temp_word[word:]
                temp_word_count += 1
            elif temp_pivot != temp_word[:word] and word <= len(temp_word) or len(temp_word) == 0:
                if temp_word_count == 1:
                    count += word
                    temp_word_count = 0
                elif temp_word_count < 10:
                    count += 1
                    count += word
                    temp_word_count = 0
                elif temp_word_count < 100:
                    count += 2
                    count += word
                    temp_word_count = 0
                elif temp_word_count < 1000:
                    count += 3
                    count += word
                    temp_word_count = 0
                elif temp_word_count == 1000:
                    count += 4
                    count += word
                    temp_word_count = 0
                temp_pivot = temp_word[:word]
                if len(temp_word) == 0:
                    break
            elif word > len(temp_word):
                if temp_word_count == 1:
                    count += word
                    temp_word_count = 0
                elif temp_word_count < 10:
                    count += 1
                    count += word
                    temp_word_count = 0
                elif temp_word_count < 100:
                    count += 2
                    count += word
                    temp_word_count = 0
                elif temp_word_count < 1000:
                    count += 3
                    count += word
                    temp_word_count = 0
                elif temp_word_count == 1000:
                    count += 4
                    count += word
                    temp_word_count = 0
                count += len(temp_word)
                break
        if 0 < count < answer:
            answer = count
    return answer

print(solution("kikikikikmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"))
