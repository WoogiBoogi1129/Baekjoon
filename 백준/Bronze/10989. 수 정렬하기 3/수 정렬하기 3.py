import sys

input = sys.stdin.readline

arr = [0] * (10000 + 1)

T = int(input())

for i in range(T):
    arr[int(input())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)