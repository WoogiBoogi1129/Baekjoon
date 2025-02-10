import sys

input = sys.stdin.readline
arr = []
T = int(input())

for _ in range(T):
    arr.append(int(input()))
    
arr.sort()

for i in arr:
    print(i)