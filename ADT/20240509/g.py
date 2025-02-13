from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B = A + A
S = sum(A)
r = 0
d = deque()
tmp = 0
ans = 1 << 60
for l in range(N):
    while r < l + N and ((d and (d[-1] == B[r] or (d[-1] + 1) % M == B[r])) or (not d)):
        d.append(B[r])
        tmp += B[r]
        r += 1

    ans = min(ans, S - tmp)

    if r == l:
        r += 1
    else:
        tmp -= d.popleft()
print(ans)
