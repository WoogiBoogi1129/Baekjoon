import sys

x, y, w, h = map(int, sys.stdin.readline().split())
result = 9999
if w/2 < x:
  result = min(result, w-x)
else:
  result = min(result, x)

if h/2 < y:
  result = min(result, h-y)
else:
  result = min(result, y)

print(result)