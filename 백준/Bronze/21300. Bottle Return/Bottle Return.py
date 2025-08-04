trashes = list(map(int, input().split()))

answer = 0

for i in trashes:
    answer += i * 5
    
print(answer)