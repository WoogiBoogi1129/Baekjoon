n = int(input())

temp = list(map(int, input().split()))

m = int(input())

arr = list(map(int, input().split()))

temp.sort()

for i in arr:
    l, r = 0, n-1
    isExist = False
    
    while l <= r:
        mid = (l + r) // 2
        if i == temp[mid]:
            isExist = True
            print(1)
            break
        elif i > temp[mid]:
            l = mid + 1
        else:
            r = mid - 1
        
    if not isExist:
        print(0)