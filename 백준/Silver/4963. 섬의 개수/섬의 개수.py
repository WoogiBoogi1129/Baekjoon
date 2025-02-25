import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    visited[x][y] = 1
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0
    
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and arr[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)