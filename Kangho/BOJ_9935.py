import sys
input = sys.stdin.readline
s = input()
s = s.rstrip()
word = input()
word = word.rstrip()
length_s = len(s)
length_word = len(word)
i = 0
check = []
check_len = 0
while i < length_s:
    check.append(s[i])
    check_len += 1
    i += 1
    if check_len >= length_word:
        for j in range(-1, -length_word-1, -1):
            if check[j] != word[j]:
                break
            else:
                a = 0
                while a < length_word:
                    check.pop()
                    check_len -= 1
                    a += 1
print(''.join(check) if check_len else 'FRULA')
