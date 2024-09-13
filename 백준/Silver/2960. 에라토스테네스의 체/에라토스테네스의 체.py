import sys

input = sys.stdin.readline

N, K = map(int, input().split())
temp = 0
check = [True] * (N+1)

for i in range(2, N + 1):
    for j in range(i, N + 1, i):
        if check[j] != False:
            check[j] = False
            temp += 1
            if temp == K:
                print(j)