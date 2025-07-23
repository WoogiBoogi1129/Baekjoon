N = int(input())
arr = list(map(int, input().split()))

temp = 1
res = 0

for i in range(N):
    if arr[i] == 1:
        res += temp
        temp += 1
        
    else:
        temp = 1
        
print(res)