n, k = map(int, input().split())
a = list(map(int, input().split()))
X = []
Y = []
s = set(a)
for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = []
for i in range(n):
    if i+1 in s:
        continue
    tmp = 10**18
    for j in range(n):
        if j+1 not in s:
            continue
        x = X[i]
        y = Y[i]
        dist = ((x-X[j])**2 + (y-Y[j])**2)**0.5

        tmp = min(tmp, dist)
    ans.append(tmp)

print(max(ans))
