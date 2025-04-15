import sys
sys.stdin = open('../sample.txt', 'r')
from queue import Queue

T = int(input())
for test_case in range(1, T+1):
    q = Queue()
    n, sunso  = map(int, input().split(" "))
    imp = list(map(int, input().split(" ")))
    for i in range(len(imp)):
        q.put((i, imp[i]))
    now_ = 0
    
    check = False
    while not check:

        cur = q.get()
        if max(imp)!=cur[1]:
            q.put(cur)
        elif cur[0]==sunso:
            now_+=1
            print(now_)
            check = True
        else:

            imp.pop(imp.index(cur[1]))
            now_+=1


