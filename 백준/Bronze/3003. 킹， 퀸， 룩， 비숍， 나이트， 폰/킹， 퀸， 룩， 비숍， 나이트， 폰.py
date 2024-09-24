import sys

input = sys.stdin.readline

temp = [1, 1, 2, 2, 2, 8]
arr = [int(x) for x in input().split()]
answer = [0] * 6
for i in range(6):
    answer[i] = temp[i] - arr[i]

for i in range(6):
    print(answer[i], end=' ')