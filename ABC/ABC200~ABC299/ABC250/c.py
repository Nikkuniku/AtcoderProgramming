n, q = map(int, input().split())
a = []
idx = []
for i in range(n):
    a.append(i+1)
    idx.append(i)
for _ in range(q):
    x = int(input())
    x -= 1
    x_idx = idx[x]
    if x_idx == n-1:
        next = a[x_idx-1]-1
        idx[x] -= 1
        idx[next] += 1
        a[x_idx], a[x_idx-1] = a[x_idx-1], a[x_idx]
    else:
        next = a[x_idx+1]-1
        idx[x] += 1
        idx[next] -= 1
        a[x_idx], a[x_idx+1] = a[x_idx+1], a[x_idx]
print(*a)
