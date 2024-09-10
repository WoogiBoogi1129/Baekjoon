n_arr = set(range(1, 10001))
non_selfnum = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    non_selfnum.add(i)

self_num = sorted(n_arr - non_selfnum)
for i in self_num:
    print(i)