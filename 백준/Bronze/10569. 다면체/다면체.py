'''
꼭짓점 수 - 모서리 수 + 면의 수 = 2
꼭짓점, 모서리 수만 셈
1 <= T <= 100
4 <= V,E <= 100 (V = 꼭짓점, E = 모서리)
'''

T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    result = V - E - 2
    print(-result)