import sys

input = sys.stdin.readline

arr = []
result = 0
for _ in range(8):
  arr.append(input())

for i in range(0, 8, 2):
  for j in range(0, 8, 2):
    if arr[i][j] == 'F':
      result += 1
    
for i in range(1, 8, 2):
  for j in range(1, 8, 2):
    if arr[i][j] == 'F':
      result += 1

print(result)