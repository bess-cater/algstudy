import sys
sys.stdin = open('../sample.txt', 'r')
from queue import Queue

T = int(input())
for test_case in range(1, T+1):
    # print(test_case)
    # print("====")
    disg = dict()
    cats = []
    n = int(input())
    for fash in range(n):
        item, category = map(str, input().split(" "))
        if not category in disg:
            disg[category]=1
            cats.append(category)
            # comb+=1
        else:
            disg[category]+=1
            # comb+=1
        
    comb = 1
    for count in disg.values():
        comb *= (count + 1)
    print(comb - 1)