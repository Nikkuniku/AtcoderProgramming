from collections import deque

N, M = map(int, input().split())
S = list(input())
T = input()
seen = [False] * N
q = deque()
for i in range(N):
    if i + M - 1 > N - 1:
        break
    isOK = True
    for j in range(M):
        if S[i + j] != T[j]:
            isOK = False
    if isOK:
        q.append(i)
while q:
    v = q.popleft()
    seen[v] = True
    for j in range(M):
        S[v + j] = "#"
    for i in range(v - M + 1, v + M):
        if i < 0 or i + M - 1 > N - 1 or seen[i]:
            continue
        isOK = True
        for j in range(M):
            if S[i + j] == "#":
                continue
            if S[i + j] != T[j]:
                isOK = False
        if isOK:
            q.append(i)
ans = "Yes" if S == ["#"] * N else "No"
print(ans)
