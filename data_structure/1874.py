import sys
from queue import LifoQueue

sys.stdin = open('sample.txt', 'r')
n = int(input())
target = []
operations = []
q = LifoQueue()
for _ in range(n):
    num = int(input())
    target.append(num)

fully = True
#[4, 3, 6, 8, 7, 5, 2, 1]
#[1, 2, 3, 4, 5]
#[1, 2, 5, 3, 4]
cur_index = 0
for i in range(1, n+1):
    q.put(i)
    operations.append("+")
    while not q.empty() and q.queue[-1] == target[cur_index]:
        q.get()
        operations.append("-")
        cur_index += 1

while cur_index < n:
    if not q.empty():
        an = q.get()
        operations.append("-")
        if an == target[cur_index]:
            cur_index+=1
    else:
        fully = False
        break



if not fully:
    print("NO")
else:
    for o in operations:
        print(o)



