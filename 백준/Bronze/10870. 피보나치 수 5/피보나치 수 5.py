N = int(input())

arr = [0] * 21
arr[1] = 1
arr[2] = 1

for i in range(3, N+1):
    arr[i] = arr[i-1] + arr[i-2]

print(arr[N])