def solution(n, arr1, arr2):
    answer = []
    bin_list = []
    for i, j in zip(arr1, arr2):
        tmp = bin(i)[2:]
        expand_range = n - len(tmp)
        for k in range(expand_range):
            tmp = "0" + tmp
        tmp2 = bin(j)[2:]
        expand_range = n - len(tmp2)
        for l in range(expand_range):
            tmp2 = "0" + tmp2
        ap_sen = ""
        for a in range(n):
            if tmp[a] == "1" or tmp2[a] == "1":
                ap_sen += "#"
            else:
                ap_sen += " "
        answer.append(ap_sen)

    return answer