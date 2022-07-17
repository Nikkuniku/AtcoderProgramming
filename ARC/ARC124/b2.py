from collections import Counter, defaultdict
n = int(input())
a = Counter(list(map(int, input().split())))
b = Counter(list(map(int, input().split())))

a = list(a.items())
b = list(b.items())

d = defaultdict(int)

for p in a:
    for q in b:
        if p[1] == q[1]:
            d[(p[0] ^ q[0])] += 1
m = len(a)
ans = []
for k, v in list(d.items()):
    if v == m:
        ans.append(k)
ans.sort()
print(len(ans))
print(*ans, sep="\n")
