import sys

input = sys.stdin.readline

N = input()

arr = [0] * 9

for i in N:
    if i == '\n':
        continue

    if i == '9':
        arr[6] += 1
    else:
        arr[int(i)] += 1

if max(arr) == arr[6]:
    check = True
    for i in range(9):
        if i == 6:
            continue
        if max(arr) == arr[i]:
            check = False
            break
    if check == True:
        if arr[6] % 2 == 0:
            print(int((arr[6] / 2)))
        else:
            print(int((arr[6] / 2) + 1))
    
    else:
        print(max(arr))

else:
    print(max(arr))
        