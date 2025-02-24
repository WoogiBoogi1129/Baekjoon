from collections import deque

N = int(input())

d = deque([int(i) for i in range(1, N+1)])

while len(d) != 1:
    d.popleft()
    d.rotate(-1)
    
print(d[0])

