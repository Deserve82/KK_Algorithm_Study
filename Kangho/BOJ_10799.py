sticks = input()

count = 0
stacks = 0
lf = False
for stick in sticks:
    if stick == '(':
        stacks += 1
        lf = True
    else:
        if lf:
            lf = False
            stacks -= 1
            count += stacks
        else:
            lf = False
            stacks -= 1
            count += 1
print(count)
