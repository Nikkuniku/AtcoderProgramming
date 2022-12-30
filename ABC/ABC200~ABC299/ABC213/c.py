h, w, n = map(int, input().split())

ans = []
a = set()
b = set()
d_a = {}
d_b = {}
for _ in range(n):
    a_i, b_i = map(int, input().split())
    ans.append([a_i, b_i])
    a.add(a_i)
    b.add(b_i)

a = sorted(list(a))
b = sorted(list(b))

for i in range(len(a)):
    d_a[a[i]] = i+1
for i in range(len(b)):
    d_b[b[i]] = i+1

for j in range(n):
    p = d_a[ans[j][0]]
    q = d_b[ans[j][1]]
    print(p, q)
