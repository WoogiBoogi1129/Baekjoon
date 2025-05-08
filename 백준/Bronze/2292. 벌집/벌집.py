N = int(input())

answer = 1

if N == 1:
    print(answer)

else:
    while N > 1:
        N -= (6*answer)
        answer += 1
        
    print(answer)