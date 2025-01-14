T = int(input())
sum = 0
for i in range(T):
    A, B = map(int, input().split())
    if A == 136:
        sum += 1000
    elif A == 142:
        sum += 5000
    elif A == 148:
        sum += 10000
    elif A == 154:
        sum += 50000

print(sum)