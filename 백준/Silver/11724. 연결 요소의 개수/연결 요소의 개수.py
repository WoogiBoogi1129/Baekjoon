from collections import deque
import sys

input = sys.stdin.readline

def bfs(x):
    visited[x] = 1
    q = deque([x])
    
    while q:
        cx = q.popleft()
        for i in adj[cx]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

N, M = map(int, input().split())

adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for _ in range(M):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
    
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1
        
print(cnt)