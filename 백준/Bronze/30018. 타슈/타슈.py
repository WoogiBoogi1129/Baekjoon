T = int(input())
cnt = 0

arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))

while arr_A != arr_B:
    for i in range(T):
        if arr_A[i] == arr_B[i]:
            continue
        if arr_A[i] > arr_B[i]:
            arr_B[i] += 1
            cnt += 1
        elif arr_A[i] < arr_B[i]:
            arr_B[i] -= 1
            cnt += 1
print(cnt // 2)