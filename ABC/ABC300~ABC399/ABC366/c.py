Q = int(input())
X = [0] * (10**6 + 1)
cnt = 0
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    t = query[0]
    if t == 1:
        x = query[1]
        if X[x] == 0:
            cnt += 1
        X[x] += 1
    elif t == 2:
        x = query[1]
        if X[x] == 1:
            cnt -= 1
        X[x] -= 1
    else:
        ans.append(cnt)
print(*ans, sep="\n")
