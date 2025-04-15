import sys
sys.stdin = open('../sample.txt', 'r')


n = int(input())
descs = dict()
max_yes = []
animals = []
for _ in range(n):
    l = list(input().split(" "))
    descs[l[0]] = []
    animals.append(l[0])
    for chars in range(2, len(l)):
        descs[l[0]].append(l[chars])

for i in range(n):
    for j in range(i + 1, n):
        shared = set(descs[animals[i]]) & set(descs[animals[j]])
        max_yes.append(len(shared)+1)
print(max(max_yes))
        
# for k, v in descs.items():
#     print(k, v)
#         if l[chars] not in descs:
#             descs[l[chars]] = []
#         descs[l[chars]].append(l[0])

# max_len = max(len(v) for v in descs.values())
# max_common_chars = [k for k, v in descs.items() if 
#                     len(v) == max_len]





