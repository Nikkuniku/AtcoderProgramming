from collections import deque
N, A, B = map(int, input().split())
S = deque(list(input()))
rotats = [''.join(S)]
for _ in range(N-1):
    S.append(S.popleft())
    rotats.append(''.join(S))
ans = [0]*N


def cost(s):
    M = len(s)
    res = 0
    for i in range(M//2):
        if s[i] != s[M-1-i]:
            res += B
    return res


for i in range(len(rotats)):
    ans[i] = cost(rotats[i])+i*A
print(min(ans))
