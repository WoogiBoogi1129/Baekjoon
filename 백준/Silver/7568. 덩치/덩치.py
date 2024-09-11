import sys

input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    temp = [int(x) for x in input().split()]
    arr.append(temp)

for i in range(len(arr)):
    rank = 1
    for j in range(len(arr)):
        if i == j:
            continue
        
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank += 1
    print(rank, end = ' ')