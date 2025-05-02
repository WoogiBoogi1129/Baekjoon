import sys

input = sys.stdin.readline

n = int(input())
ans = 1
for _ in range(n):
    ans += (int(input()) - 1)
    
print(ans)