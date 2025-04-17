import sys
sys.stdin = open('../sample.txt', 'r')
import heapq


n, k = map(int, input().split(" "))
kachi = [[] for i in range(12)]

for i in range(n):
    position, value = map(int, input().split(" "))
    heapq.heappush(kachi[position], -value)

# cur_index = [-1 for i in range(12)]
for _ in range(k):
    selected = []
    for i in range(1, 12):
        if kachi[i]:
            top = -heapq.heappop(kachi[i])  # max value
            selected.append((i, top)) 
            if top > 0:
                heapq.heappush(kachi[i], -(top - 1))      # store selected for later
        else:
            selected.append((i, 0))

result = 0
for i in range(1, 12):
    if kachi[i]:
        result += -heapq.heappop(kachi[i])
print(result)



