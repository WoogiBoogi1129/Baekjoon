import sys
input = sys.stdin.readline

MOD = 1000000009
MAX_N = 100000

dp = [[0] * 4 for _ in range(MAX_N + 1)]

dp[1][1] = 1
dp[2][2] = 1
dp[3][3] = 1
dp[3][1] = 1
dp[3][2] = 1

for i in range(4, MAX_N + 1):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD
    
data = input().split()
t = int(data[0])
for i in range(1, t + 1):
    n = int(input())
    print((dp[n][1] + dp[n][2] + dp[n][3]) % MOD)