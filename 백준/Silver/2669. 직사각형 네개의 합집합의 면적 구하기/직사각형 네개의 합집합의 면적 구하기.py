arr = []
for _ in range(101):
    temp = [0] * 101
    arr.append(temp)
    
answer = 0

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            if arr[i][j] == 0:
                arr[i][j] = 1

for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            answer += 1
            
print(answer)