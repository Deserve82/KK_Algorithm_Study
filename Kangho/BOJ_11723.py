import sys
curr_state = 0
N = int(sys.stdin.readline())
for _ in range(N):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        num = command[1]
        command = command[0]
        if command == 'add':
            curr_state |= (1 << int(num))
        elif command == 'remove':
            curr_state &= ~(1 << int(num))
        elif command == 'check':
            if curr_state & (1 << int(num)):
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            curr_state ^= (1 << int(num))
    else:
        if command[0] == 'all':
            curr_state = (1 << 20) - 1
        else:
            curr_state = 0
