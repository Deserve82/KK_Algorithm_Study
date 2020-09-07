n = int(input())
m = int(input())
if m > 0:
    malf = input().split()
else:
    malf = []
 
channels = []
curr = 100
 
for c in range(0, 1000000+1):
    isCont = True
    for str_c in str(c):
        if str_c in malf:
            isCont = False
            break
    if isCont:
        channels.append(c)
 
min_diff = 987654321
val = ''
for i in channels:
    if abs(i-n) < min_diff:
        min_diff = abs(i-n)
        val = str(i)
 
answer = len(val)+abs(min_diff)
 
answer = min(abs(n-curr), answer)
 
print(answer)
