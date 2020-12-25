def get_proper_bracket():
    bra_basket = []
    good_bracket = True
    for s in string:
        if s == '(' or s == '{' or s == '[':
            bra_basket.append(s)
        else:
            if not bra_basket:
                return False
            top = bra_basket.pop()
            if s == ')' and top != '(':
                return False
            elif s == '}' and top != '{':
                return False
            elif s == ']' and top != '[':
                return False
    if bra_basket:
        good_bracket = False
    return good_bracket


for _ in range(int(input())):
    string = input()
    if get_proper_bracket():
        print("YES")
    else:
        print("NO")
