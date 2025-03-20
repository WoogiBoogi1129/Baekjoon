t, ans = map(int, input().split())

for _ in range(t):
    a, b = map(int, input().split())
    ans += a
    ans -= b
    
print("비와이")