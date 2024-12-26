n = int(input())

line = 0
end = 0

while end < n:
    line += 1
    end += line

k = end-n

if line % 2 == 0:
    a = line-k
    b = k+1
else:
    a = k+1
    b = line-k

print(str(a)+'/'+str(b))