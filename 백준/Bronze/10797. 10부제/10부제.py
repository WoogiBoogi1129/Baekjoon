day = int(input())
cars = list(map(int, input().split()))
cnt = 0

for i in cars:
    if day == i:
        cnt += 1
        
print(cnt)