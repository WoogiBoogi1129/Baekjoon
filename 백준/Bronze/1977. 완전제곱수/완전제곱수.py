M = int(input())
N = int(input())
ans = []
res = 0
for i in range(M, N+1):
    if (i ** (1/2)) % 1 == 0:
        ans.append(i)
        res += i

if len(ans) == 0:
    print(-1)

else:
    print(res)
    print(ans[0])