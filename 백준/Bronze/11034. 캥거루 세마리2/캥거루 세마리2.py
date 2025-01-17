while True:
    try:
        A, B, C = map(int, input().split())
        if C-B >= B-A:
            result = C-B-1
        else:
            result = B-A-1
        print(result)
    except:
        break