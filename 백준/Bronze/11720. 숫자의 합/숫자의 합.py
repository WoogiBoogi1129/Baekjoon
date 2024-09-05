import sys

input = sys.stdin.readline

N = int(input())

arr = input()

result = 0
for i in range(len(arr)-1):
  result += int(arr[i])

print(result)