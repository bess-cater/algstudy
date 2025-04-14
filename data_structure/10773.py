import sys

sys.stdin = open('sample.txt', 'r')

k  = int(input())
hap = 0
collect = []
for _ in range(k):
    new_n = int(input())
    if new_n!=0:
        collect.append(new_n)
        hap+=new_n
    else:
        if collect:
            popped = collect.pop()
            hap-=popped
print(hap)