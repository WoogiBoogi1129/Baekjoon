import sys
input = sys.stdin.readline

T = int(input())

arr = []

for _ in range(T):
    arr.append(input().strip())
    
arr = list(set(arr))
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)