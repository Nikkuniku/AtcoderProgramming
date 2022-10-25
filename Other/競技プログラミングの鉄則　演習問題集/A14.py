n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

ab = []
cd = set()
for i in range(n):
    for j in range(n):
        ab.append(a[i]+b[j])
        cd.add(c[i]+d[j])

for p in ab:
    if k-p in cd:
        print('Yes')
        exit()
print('No')
