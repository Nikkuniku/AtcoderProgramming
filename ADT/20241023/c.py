N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))
masu = [0] * (N + 1)
for a in A:
    masu[a] += 1
for l in L:
    cnt = 0
    for i in range(1, N + 1):
        if masu[i] == 1:
            cnt += 1
        if cnt == l:
            if i == N:
                continue
            else:
                if masu[i + 1] == 0:
                    masu[i + 1] = 1
                    masu[i] = 0
                    break
ans = []
for i in range(1, N + 1):
    if masu[i]:
        ans.append(i)
print(*ans)
