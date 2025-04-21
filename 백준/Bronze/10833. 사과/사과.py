N = int(input())
result = 0

for _ in range(N):
    students, apples = map(int, input().split())
    result += apples % students
    
print(result)