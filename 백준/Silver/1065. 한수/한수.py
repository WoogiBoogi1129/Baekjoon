N = int(input())

cnt = 0
for x in range(1, N+1):
    if x <= 99:
        cnt += 1
    
    else:    
        a = (x // 100)
        d = ((x % 100) // 10) - a
        
        if (x % 10) - d == ((x % 100) // 10):
            cnt += 1
        
print(cnt)