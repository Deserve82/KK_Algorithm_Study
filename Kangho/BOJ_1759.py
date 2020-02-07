password_length, word_length = map(int, input().split())
a_list = list(input().split())
a_list.sort()
word_count = 0
password = []
check = [False]*word_length
vowels = ['a', 'e', 'i', 'o', 'u']
l = []

def p(word_count, point):
    if word_count == password_length:
        temp_v = 0
        temp_else = 0
        for i in password:
            if i in vowels:
                temp_v += 1
            else:
                temp_else +=1
        if temp_v > 0 and temp_else > 1:
            l.append(("".join(map(str, password))))
        return
    else:
        for i in range(point, len(a_list)):
            if not check[i]:
                check[i] = True
                password.append(a_list[i])
                p(word_count+1, i)
                password.pop()
                check[i] = False
p(0, 0)
for i in l:
    print(i)