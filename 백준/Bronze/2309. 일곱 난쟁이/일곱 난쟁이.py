arr = []

for i in range(9):
    arr.append(int(input()))

arr.sort()
arr_sum = sum(arr)
check = True
for i in range(9):
    if check == False:
        break
    for j in range(9):
        if i == j:
            continue
        if arr_sum - (arr[i] + arr[j]) == 100:
            arr[i] = 0
            arr[j] = 0
            check = False
            break

for i in range(9):
    if arr[i] == 0:
        continue
    print(arr[i])