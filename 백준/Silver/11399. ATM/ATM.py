N = int(input())

a = map(int, input().split())
arr = list(a)

arr.sort()

for i in range(1, len(arr)):
    arr[i] += arr[i-1]
    
print(sum(arr))