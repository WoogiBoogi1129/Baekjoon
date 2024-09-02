import sys

A, B = sys.stdin.readline().split()

min_ans = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_ans = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(min_ans, max_ans)