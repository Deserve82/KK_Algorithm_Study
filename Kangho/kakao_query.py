def solution(info, query):
    answer = []
    for q in query:
        counter = 0
        customized_filter = ["", "", "", "", 0]
        jp, z, fb, z, js, z, pc, score = q.split(" ")
        customized_filter[0] = jp
        customized_filter[1] = fb
        customized_filter[2] = js
        customized_filter[3] = pc
        customized_filter[4] = int(score)
        for information in info:
            fit_all_counter = 0
            jp, fb, js, pc, score = information.split(" ")
            if customized_filter[0] == jp or customized_filter[0] == '-':
                fit_all_counter += 1
            if customized_filter[1] == fb or customized_filter[1] == '-':
                fit_all_counter += 1
            if customized_filter[2] == js or customized_filter[2] == '-':
                fit_all_counter += 1
            if customized_filter[3] == pc or customized_filter[3] == '-':
                fit_all_counter += 1
            if customized_filter[4] <= int(score):
                fit_all_counter += 1
            if fit_all_counter == 5:
                counter += 1
        answer.append(counter)
    print(answer)
    return answer


i = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
q = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]
solution(i, q)
