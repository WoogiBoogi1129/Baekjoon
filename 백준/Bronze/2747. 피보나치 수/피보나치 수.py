def fibo(n):
    if n <= 1:
        return arr[n]
    return arr[n-1] + arr[n-2]

arr = []
arr.append(0)
arr.append(1)

N = int(input())

for i in range(2, N+1):
    arr.append(fibo(i))

print(arr[N])