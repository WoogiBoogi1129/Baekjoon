import sys

target = int(sys.stdin.readline())
cnt = 0
temp = target
  
while True:  
  first = target // 10
  second = target % 10
  third = (first + second) % 10
  target = (second * 10) + third
  cnt += 1
  if target == temp:
    break

print(cnt)