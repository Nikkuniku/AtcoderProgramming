n, m = map(int, input().split())
edges = [0]*(n+2)
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    if a > b:
        a, b = b, a
    edges[a] += 1
    edges[b] -= 1

for i in range(1, len(edges)):
    edges[i] += edges[i-1]
ans = 'YES'
for j in range(len(edges)):
    if edges[j] % 2 != 0:
        ans = 'NO'
        break
print(ans)
