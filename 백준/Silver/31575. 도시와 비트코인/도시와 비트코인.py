def dfs(x, y):
    visited[x][y] = 1
    
    if visited[M-1][N-1] == 1:
        return 1
    
    dx = [0, 1]
    dy = [1, 0]
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == 0 and m[nx][ny] == 1:
            if dfs(nx, ny):
                return 1
    return 0

N, M = map(int, input().split())

m = [list(map(int, input().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]

if dfs(0, 0):
    print("Yes")
else:
    print("No")