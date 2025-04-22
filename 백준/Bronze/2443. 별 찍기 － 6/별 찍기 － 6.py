N = int(input())

for i in range(N):
    for j in range(i):
        print(" ", end='')
    for k in range(N-i, 0, -1):
        print("*", end='')
    for l in range(N-1-i, 0, -1):
        print("*", end='')
    print("")