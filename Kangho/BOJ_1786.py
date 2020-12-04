def get_fail(pat):
    pat_len = len(pat)
    fail = [0] * (pat_len + 1)

    j = 0
    for i in range(1, pat_len):
        while j > 0 and pat[i] != pat[j]:
            j = fail[j - 1]

        if pat[i] == pat[j]:
            j += 1
            fail[i] = j
        else:
            fail[i] = j
    return fail


def kmp(text, fail, pat):
    text_len = len(text)
    pat_len = len(pat)
    answer_count = 0
    answer_list = []
    print(fail)
    j = 0
    for i in range(text_len):
        while j > 0 and text[i] != pat[j]:
            j = fail[j - 1]
        if text[i] == pat[j]:
            if j == pat_len - 1:
                answer_count += 1
                answer_list.append((i - j) + 1)
                j = fail[j]
            else:
                j += 1
    return answer_count, answer_list


txt = input()
par = input()
a, b = kmp(txt, get_fail(par), par)
print(a)
b = list(map(str, b))
print(" ".join(b))
