N, M = map(int, input().split())

A_table = [list(map(int, input().split())) for _ in range(N)]
B_table = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        print(A_table[i][j] + B_table[i][j], end=' ')
    print()