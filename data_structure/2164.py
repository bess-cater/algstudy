import sys
from queue import Queue

sys.stdin = open('sample.txt', 'r')
q = Queue()
k  = int(input())
for i in range(1, k+1):
    q.put(i)

# a = [i ]
while q.qsize()>1:
    p = q.get()
    q.put(q.get())

print(q.get())

