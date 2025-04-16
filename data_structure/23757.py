import sys
sys.stdin = open('../sample.txt', 'r')
from queue import PriorityQueue

prQueue = PriorityQueue()
n, m = map(int, input().split(" "))
presents = list(map(int, input().split(" ")))
children = list(map(int, input().split(" ")))
possible = True
for i in range(len(presents)):
    prQueue.put((presents[i]*-1, i))

for child in children:
    present = prQueue.get()
    if child>(present[0]*-1):
        possible = False
        break
    #if still left?
    if (present[0]*-1)>child:
        
        prQueue.put((present[0]+child, present[1]))
if possible:
    print("1")
else:
    print("0")

