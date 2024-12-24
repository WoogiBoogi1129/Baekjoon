T = int(input())

for i in range(T):
    Q = D = N = P = 0
    C = int(input())
    Q = int(C / 25)
    C %= 25
    D = int(C / 10)
    C %= 10
    N = int(C / 5)
    C %= 5
    P = C
    print(Q, D, N, P)
    