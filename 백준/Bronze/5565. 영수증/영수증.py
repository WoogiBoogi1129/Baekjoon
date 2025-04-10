total_cost = int(input())
arr_cost = []
for _ in range(9):
    arr_cost.append(int(input()))

result = total_cost - sum(arr_cost)

print(result)