import sys
input = sys.stdin.readline

grade = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}

# 전공평점 = (학점 * 과목평점)sum / 학점총합 
sum = 0
major_point = 0
cal_cnt = 0

for _ in range(20):
    a, b, c = map(str, input().split())
    if c == 'P':
        continue
    
    major_point += float(b)
    sum += (float(b) * float(grade[c]))

print(sum / major_point)