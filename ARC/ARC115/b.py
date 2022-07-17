n = int(input())
c = []
for _ in range(n):
    c.append(list(map(int, input().split())))

a = [0]
# 最初にBを求める
b = []
for j in range(n):
    b.append(c[0][j])
# Aを求めていく
ans = 'Yes'
for i in range(1, n):
    p = set()
    for j in range(n):
        p.add(c[i][j]-b[j])

    if len(p) == 1:
        a.append(min(p))
    else:
        ans = 'No'
        print(ans)
        exit(0)
a_min = min(a)
if a_min < 0:
    for i in range(n):
        a[i] -= a_min
        b[i] += a_min
print(ans)
print(*a)
print(*b)
