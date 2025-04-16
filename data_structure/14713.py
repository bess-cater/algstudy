import sys
sys.stdin = open('../sample.txt', 'r')
from queue import Queue

final_s = Queue()
possible = True
n = int(input())
parrot_words = []
cur_word_indeces = [0 for i in range(n)] # [0, 0, 0]
for nn in range(n):
    words = list(map(str, input().split(" ")))
    parrot_words.append(words)
sent = list(map(str, input().split(" ")))
for s in sent:
    final_s.put(s)
# print(parrot_words)
# print(final_s.queue)
while not final_s.empty():
    found = False
    cur_word = final_s.get()
    # print(cur_word)
    for i in range(len(parrot_words)):
        if cur_word_indeces[i]>(len(parrot_words[i]))-1:
            continue
        if parrot_words[i][cur_word_indeces[i]]==cur_word:
            # print("found!!")
            # print(parrot_words[i])
            cur_word_indeces[i]+=1
            # print(cur_word_indeces)
            found = True
            break
    if not found:
        possible = False
        break
for k, v in zip(parrot_words, cur_word_indeces):
    if len(k)!=v:
        possible=False
        break

if possible:
    print("Possible")
else:
    print("Impossible")
