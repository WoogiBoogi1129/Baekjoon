import sys

T = sys.stdin.readline()
arr = [int(x) for x in sys.stdin.readline().split()]

ans = 1

for i in range(1, len(arr)):
  if arr[i] >= arr[i-1]:
    ans += 1
print(ans)