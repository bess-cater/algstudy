import sys
sys.stdin = open('../sample.txt', 'r')

#To be run in PyPy3, not Pyrhon3!!!

left_stack = list(input().strip())
right_stack = []
n = int(input())

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif cmd[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif cmd[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif cmd[0] == 'P':
        left_stack.append(cmd[1])

print(''.join(left_stack + right_stack[::-1]))
