s = input()


def is_palin(index):
    length = len(s)-1
    for i in range(index, length):
        if s[i] != s[length]:
            return False
        length -= 1
    return True


ll = len(s)
for i in range(ll):
    if is_palin(i):
        print(ll + i)
        break
