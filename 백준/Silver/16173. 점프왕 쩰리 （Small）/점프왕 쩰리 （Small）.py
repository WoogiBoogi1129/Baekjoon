"""
dfs 아래 오른쪽 고려하기
가장 오른쪽 가장 아래칸 도착하면 승리
쩰리가 한번에 이동할 수 있는 칸의 수가 현재 밟고 있는 칸의 수만큼임
"""
def dfs(x, y):
    visit[x][y] = True
    
    dx = [m[x][y], 0]
    dy = [0, m[x][y]]
    
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
            dfs(nx, ny)
    
m = []

N = int(input())

visit = [[0] * N for _ in range(N)]

for i in range(N):
    m.append(list(map(int, input().split())))

dfs(0, 0)

if visit[N-1][N-1] == True:
    print("HaruHaru")
else:
    print("Hing")