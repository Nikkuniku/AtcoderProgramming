N, M = map(int, input().split())
A = list(map(int, input().split()))

if 1 in set(A) or N in set(A):
    exit(print(-1))

B = [True] * (N + 1)
for a in A:
    B[a] = False

ans = []
now = 1
stop = -1
while len(ans) < N:
    if B[now]:
        ans.append(now)
        now += 1
    else:
        stop = now
        now += 1
        while not B[now]:
            ans.append(now)
            now += 1
        ans.append(now)
        ans.append(stop)
        now += 1
print(*ans)
