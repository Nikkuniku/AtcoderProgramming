N, K = map(int, input().split())
V = list(map(int, input().split()))
ans = 0
for a in range(N+1):
    for b in range(N+1):
        if a+b > N:
            continue
        nokori = K-(a+b)
        if a+b > K:
            continue

        tmp = []
        for i in range(a):
            tmp.append(V[i])
        for j in range(b):
            tmp.append(V[::-1][j])

        tmp.sort(reverse=True)
        while tmp and nokori:
            if tmp[-1] < 0:
                tmp.pop()
                nokori -= 1
            else:
                break
        ans = max(ans, sum(tmp))
print(ans)
