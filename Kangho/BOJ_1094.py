X = int(input())
stick = 64
stick_count = 0
while X:
    if X < stick:
        stick /= 2
    else:
        X -= stick
        stick_count += 1

print(stick_count)