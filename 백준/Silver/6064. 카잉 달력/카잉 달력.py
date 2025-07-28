import math

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    lcm = math.lcm(M, N)
    result = -1
    
    # i는 x에서 시작해서 M씩 증가 (x + M*k 형태)
    for i in range(x, lcm + 1, M):
        # y 증가 규칙은 (i - 1) % N + 1
        if (i - 1) % N + 1 == y:
            result = i
            break

    print(result)