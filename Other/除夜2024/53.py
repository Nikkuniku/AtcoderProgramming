N, A = map(int, input().split())
T = list(map(int, input().split()))
ans = []
now = 0
for i in range(N):
    if now <= T[i]:
        ans.append(T[i] + A)
        now = T[i] + A
    else:
        ans.append(now + A)
        now += A
print(*ans, sep="\n")
