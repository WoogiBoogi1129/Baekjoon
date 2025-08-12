'''
술 초밥 or 점심 아닐 때 = 280
점심 and 술X 일때 = 320
'''

time, S = map(int, input().split())

if S == 1 or 0 <= time <= 11 or 17 <= time <= 23:
    print(280)
elif S == 0 and 12 <= time <= 16:
    print(320)