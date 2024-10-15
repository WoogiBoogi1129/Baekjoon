N, M = map(int, input().split())
card = list(map(int, input().split()))
max_number = 0
for i in range(len(card)):
    for j in range(len(card)):
        for k in range(len(card)):
            if i == j or i == k or j == k:
                continue

            temp = card[i] + card[j] + card[k]
            if temp > max_number and temp <= M:
                max_number = temp

print(max_number)