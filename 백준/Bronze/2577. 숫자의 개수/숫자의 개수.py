arr = [0] * 10

A = int(input())
B = int(input())
C = int(input())

temp = A * B * C

for i in str(temp):
    arr[int(i)] += 1

for i in range(0, 10):
    print(arr[i])
