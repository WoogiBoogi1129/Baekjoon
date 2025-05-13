N, A, B = map(int, input().split())

if A < B:
    print("Bus")
elif B >= N and B < A:
    print("Subway")
else:
    print("Anything")