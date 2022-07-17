n = int(input())
dish = []
for _ in range(n):
    a, b = map(int, input().split())
    dish.append((a, b, a+b))

# dish.sort(key=lambda x: x[0], reverse=True)
dish.sort(key=lambda x: x[2], reverse=True)

takahashi = 0
aoki = 0
for i in range(n):
    if i % 2 == 0:
        takahashi += dish[i][0]
    else:
        aoki += dish[i][1]

print(takahashi-aoki)
