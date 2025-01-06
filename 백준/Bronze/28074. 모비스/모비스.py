x = input()

if len(x) < 5:
    print("NO")

else:
    if x.find('M') != -1 and x.find('O') != -1 and x.find('B') != -1 and x.find('I') != -1 and x.find('S') != -1:
        print("YES")
    else:
        print("NO")