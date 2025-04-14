# import sys
# sys.stdin = open('sample.txt', 'r')

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = int(input())
b = list(map(int, input().split()))

def check(num, start, end):
    if start > end:
        return False
    middle = (start + end) // 2
    if a[middle] == num:
        return True
    elif num < a[middle]:
        return check(num, start, middle - 1)
    else:
        return check(num, middle + 1, end)

for el in b:
    in_list = check(el, 0, n - 1)
    print("1" if in_list else "0")


