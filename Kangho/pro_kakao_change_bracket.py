def check(p):
    right_str_check = 0
    flag = True
    for i in p:
        if i == '(':
            right_str_check += 1
        elif i == ')':
            right_str_check -= 1
        if right_str_check < 0:
            flag = False
            break
    if flag:
        return True
    else:
        return False


def re(p):
    if check(p):
        return p

    s_bracket = 0
    e_bracket = 0
    for i in p:
        if i == '(':
            s_bracket += 1
        elif i == ')':
            e_bracket += 1
        if s_bracket == e_bracket:
            u = p[:s_bracket + e_bracket]
            v = p[s_bracket + e_bracket:]
            if check(u):
                return u + re(v)
            else:
                value = '(' + re(v) + ')'
                u = u[1:-1]
                fixed_u = []
                for j in u:
                    if j == ')':
                        fixed_u.append('(')
                    else:
                        fixed_u.append(')')
                return value + "".join(fixed_u)

print(re(")()()()("))
