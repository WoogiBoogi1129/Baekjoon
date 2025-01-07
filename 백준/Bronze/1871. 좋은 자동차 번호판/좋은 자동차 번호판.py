# 1가치 + 2가치 < 100
# 26^2 + (알파벳 자리수)
T = int(input())

for i in range(T):
    S = input()
    A,B = S.split('-')
    
    temp = abs(((ord(A[0]) - ord('A')) * (26**2)) + ((ord(A[1]) - ord('A')) * (26**1)) + ((ord(A[2]) - ord('A')) * (26**0)) - int(B))
    
    if temp <= 100:
        print("nice")
    else:
        print("not nice")