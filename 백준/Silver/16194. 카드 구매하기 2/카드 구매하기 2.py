N = int(input())
P = list(map(int, input().split()))

dp = [float('inf')] * (N + 1)
dp[0] = 0 

for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = min(dp[i], dp[i - j] + P[j - 1])

print(dp[N])