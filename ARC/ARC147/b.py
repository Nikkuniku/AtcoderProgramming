n = int(input())
p = list(map(int, input().split()))
cnt = 0
ans = []
pos = [-1]*(n+1)
s = set()
for i in range(n):
    if i % 2 == p[i] % 2:
        cnt += 1
        s.add(p[i])
    pos[p[i]] = i
cnt //= 2
pla = [False]*n
for k in range(n):
    if k % 2 != p[k] % 2:
        continue
    c = p[k]
    while not pla[pos[c]]:
        i = pos[c]
        j = pos[c]-2
        if j >= 0 and not pla[j]:
            ans.append(('B', j))
            pos[p[i]], pos[p[j]] = pos[p[j]], pos[p[i]]
            p[i], p[j] = p[j], p[i]
        else:
            pla[pos[c]] = True

for i in range(cnt):
    ans.append(('A', 2*i))
    pos[p[2*i]], pos[p[2*i+1]] = pos[p[2*i+1]], pos[p[2*i]]
    p[2*i], p[2*i+1] = p[2*i+1], p[2*i]

for c in range(1, n+1):
    if pos[c] == c-1:
        continue
    while pos[c] != c-1:
        i = pos[c]
        j = pos[c]-2
        ans.append(('B', j))
        pos[p[i]], pos[p[j]] = pos[p[j]], pos[p[i]]
        p[i], p[j] = p[j], p[i]
if ans:
    print(len(ans))
    for s, t in ans:
        print(s, t+1)
else:
    print(0)
