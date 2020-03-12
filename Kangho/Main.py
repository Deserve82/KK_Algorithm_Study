n = int(input())
dynamic = [0]*101
dynamic[1], dynamic[2] = 9, 17


def dp(number):
    if number == 1:
        return dynamic[1]
    elif number == 2:
        return dynamic[2]
    elif dynamic[number] != 0:
        return dynamic[number]
    else:
        dynamic[number] = (dp(number-1)*2 - (number-1)) % 1000000000
        return dynamic[number]


print(dp(n))
