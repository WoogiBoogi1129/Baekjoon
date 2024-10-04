import sys

input = sys.stdin.readline

s = []
avg = 0
for _ in range(5):
    temp = int(input())
    s.append(temp)
    avg += temp
s.sort()

print(int(avg/ 5))
print(s[int(5/2)])