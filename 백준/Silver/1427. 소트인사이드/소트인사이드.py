arr = input()
arr = int(arr)

temp = []
while True:
    if arr < 10:
        temp.append(arr % 10)
        break
    temp.append(arr % 10)
    arr = arr // 10
    
temp.sort()
temp.reverse()

for i in temp:
    print(i, end='')