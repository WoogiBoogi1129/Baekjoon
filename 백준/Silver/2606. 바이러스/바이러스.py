def dfs(start):
    visited[start] = 1
    for nx in adj[start]:
        if visited[nx] == 0:
            dfs(nx)
    
N = int(input())
V = int(input())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(V):
    x, y = map(int, input().split())
    adj[x]+=[y]
    adj[y]+=[x]

dfs(1)

print(sum(visited)-1)