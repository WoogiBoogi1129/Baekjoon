T = int(input())

for _ in range(T):
    ans = int(input())
    num = int(input())
    for i in range(num):
        p, q = map(int, input().split())
        ans += (p * q)
        
    print(ans)