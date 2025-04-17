import sys
sys.stdin = open('../sample.txt', 'r')
from collections import deque

n, k = map(int, input().split(" "))
left = n
dq1 = deque()
dq2 = deque()

#first setting

for i in range(1, n+1):
    if i == 1:
        dq1.append(i)
    else: 
        dq2.append(i)


while len(dq1)+len(dq2)>k:
    for times in range(k-1):
        dq2.popleft()

    dq2.append(dq1.pop())
    dq1.append(dq2.popleft())

print(dq1[0])
