from collections import Counter as mset

def clean_text(read_data):
    for i in read_data:
        if i not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    l1 = len(str1)
    l2 = len(str2)
    st1 = []
    st2 = []
    for i in range(l1-1):
        test = str1[i:i+2]
        if clean_text(test):
            st1.append(test)
    for i in range(l2-1):
        test = str2[i:i+2]
        if clean_text(test):
            st2.append(test)
    if len(st1) == 0 and len(st2) == 0:
        return 65536
    mst1 = mset(st1)
    mst2 = mset(st2)
    inter_lst = list((mst1 & mst2).elements())
    len_inter_lst = len(inter_lst)
    len_union_lst = len(st1) + len(st2) - len_inter_lst
    return int((len_inter_lst/len_union_lst)*65536)

print(solution("", ""))
