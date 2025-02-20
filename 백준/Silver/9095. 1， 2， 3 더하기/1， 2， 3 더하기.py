T = int(input())

for _ in range(T):
    dp = [0] * 11
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    
    n = int(input())
    if n <= 3:
        print(dp[n-1])
        
    else:
        for i in range(3, n):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
            
        print(dp[n-1])