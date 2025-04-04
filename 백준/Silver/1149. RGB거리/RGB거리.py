n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = arr

for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i][j] + dp[i-1][j+1], dp[i][j] + dp[i-1][j+2])
        elif j == 1:
            dp[i][j] = min(dp[i][j] + dp[i-1][j-1], dp[i][j] + dp[i-1][j+1])
        else:
            dp[i][j] = min(dp[i][j] + dp[i-1][j-1], dp[i][j] + dp[i-1][j-2])

result = min(dp[n-1])

print(result)