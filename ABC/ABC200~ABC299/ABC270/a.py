a, b = map(int, input().split())
snuke = 0
for i in range(3):
    if a & (1 << i):
        snuke |= 1 << i
    if b & (1 << i):
        snuke |= 1 << i
print(snuke)
