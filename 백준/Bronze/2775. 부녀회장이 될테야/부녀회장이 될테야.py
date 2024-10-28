# 아파트 거주조건
# a층 b호에 사는 조건
# (a-1)층의 1 ~ b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 함.

# k층 n호에는 몇 명이 살고 있는지 출력하자.

# 아파트는 0층부터 존재 / 각층에는 1호부터 존재 / 0층의 i 호에는 i명이 삼

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    for i in range(1, n + 1):
        dp[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(dp[k][n])