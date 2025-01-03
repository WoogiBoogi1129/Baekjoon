T = int(input())
while T:
    A, B, X = map(int, input().split())
    result = A * (X - 1) + B
    print(result)
    T -= 1