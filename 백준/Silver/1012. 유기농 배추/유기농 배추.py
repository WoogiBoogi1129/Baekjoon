import sys 
sys.setrecursionlimit(10000) 

def dfs(x, y):
    visited[x][y] = True
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and field[nx][ny] == 1:
            dfs(nx, ny)
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    
    for i in range(K):
        y, x = map(int, input().split())
        field[x][y] = 1
        
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == False:
                dfs(i,j)
                cnt += 1
                
    print(cnt)