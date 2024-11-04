E, S, M = map(int, input().split())
result = 0
e = s = m = 1
while True:
    if e == E and s == S and m == M:
        result += 1
        break
    e += 1
    s += 1
    m += 1

    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
    result += 1
print(result)