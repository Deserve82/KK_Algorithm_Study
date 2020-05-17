n = input()
bf = False
if len(n)>1:
    if 2 < int(n[0]) and n[1] == '0':
        bf = True
dp = [0] * (len(n))
dp[0] = 1
previous_char = n[0]
for i, c in enumerate(n):
    if i == 1:
        if previous_char == '1' and c != '0':
            dp[1] = 2
            previous_char = c
        elif previous_char == '2' and 0 < int(c) < 7:
            dp[1] = 2
            previous_char = c
        else:
            dp[1] = 1
            previous_char = c
    elif i == 0:
        continue
    elif previous_char == '1' and c != '0':
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
        previous_char = c
    elif previous_char == '2' and 0 < int(c) < 7:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
        previous_char = c
    elif (previous_char == '1' or previous_char == '2') and c == '0':
        dp[i-1] = dp[i-2]
        dp[i] = dp[i-1]
        previous_char = c
    elif c == '0' and 2 < int(previous_char):
        bf = True
        break
    elif c == '0' and previous_char == '0':
        bf = True
        break
    else:
        dp[i] = dp[i - 1]
        previous_char = c

if n[0] == '0':
    print(0)
elif bf:
    print(0)
else:
    print(dp[-1] % 1000000)

