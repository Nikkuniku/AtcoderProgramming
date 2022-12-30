from itertools import combinations
x = int(input())
bit = []
for i in range(62):
    if (x & (1 << i)):
        bit.append(i)
ans = []

for i in range(len(bit)+1):
    p = combinations(bit, i)
    for pet in p:
        tmp = 0
        for j in range(i):
            tmp += 1 << pet[j]
        ans.append(tmp)
ans.sort()
print(*ans, sep="\n")
