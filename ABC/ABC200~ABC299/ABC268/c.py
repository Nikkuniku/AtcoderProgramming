n = int(input())
p = list(map(int, input().split()))

pos = [-1]*n
for i in range(n):
    if p[i] > i:
        pos[p[i]] = i+1+n-1-p[i]
    elif p[i] == i:
        pos[p[i]] = 0
    else:
        pos[p[i]] = i-p[i]

dist = [0]*n
for c in pos:
    dist[c] += 1
dist += dist
ans = 0
for i in range(n):
    tmp = dist[i:i+3]
    ans = max(ans, sum(tmp))
print(ans)
