A, B = map(int, input().split())

A = B - A

for i in range(9, 0, -1):
    if A % i == 0 and B % i == 0:
        A = A // i
        B = B // i
        break

print(A, B)