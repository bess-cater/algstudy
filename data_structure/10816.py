import sys

nums = dict()
sys.stdin = open('sample.txt', 'r')
n = int(input())
a = list(map(int, input().split()))
m = int(input())
to_find = list(map(int, input().split()))

for an in a:
    if an in nums.keys():
        nums[an]+=1
    else:
        nums[an]=1

for bn in to_find:

    if bn in nums.keys():
        print(nums[bn], end = " ")  # end = ""
    else: print("0",  end = " ")