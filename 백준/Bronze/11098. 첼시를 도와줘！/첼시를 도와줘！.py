t = int(input())
for _ in range(t):
    n = int(input())
    res = 0
    
    for _ in range(n):
        cost, name = input().split()
        cost = int(cost)
        
        if res < cost:
            res = cost
            ans = name
    
    print(ans)