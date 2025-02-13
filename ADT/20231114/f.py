N = int(input())
bits = []
for i in range(60):
    if N & (1 << i):
        bits.append(i)
ans = []
for i in range(1 << len(bits)):
    tmp = 0
    for j in range(len(bits)):
        if i & (1 << j):
            tmp |= 1 << bits[j]
    ans.append(tmp)
print(*ans, sep="\n")
