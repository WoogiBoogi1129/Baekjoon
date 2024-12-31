N = int(input())

for i in range(N, 0, -1):
    for j in range(i-1):
        print(" ", end='')
    for k in range(N-i+1):
        print("*", end='')
    for a in range(N-i):
        print("*", end='')
    print("")