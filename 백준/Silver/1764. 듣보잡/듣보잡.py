N, M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(input())
    
for _ in range(M):
    arr.append(input())
    
arr.sort()

cnt = 0
result = []
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        cnt += 1
        i += 1
        result.append(arr[i])
        
print(cnt)
for i in result:
    print(i)