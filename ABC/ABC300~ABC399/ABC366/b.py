from collections import deque

N = int(input())
S = [list(input()) for _ in range(N)]
M = 0
for s in S:
    M = max(M, len(s))
ans = [deque() for _ in range(M)]
for i in range(N):
    for j in range(M):
        if j >= len(S[i]):
            if not ans[j]:
                continue
            else:
                ans[j].appendleft("*")
        else:
            ans[j].appendleft(S[i][j])
for c in ans:
    print(*c, sep="")
