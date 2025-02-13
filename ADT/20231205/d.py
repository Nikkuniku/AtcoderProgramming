N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
ans = 0
for i in range(N):
    for j in range(M):
        if S[i].endswith(T[j]):
            ans += 1
            break
print(ans)
