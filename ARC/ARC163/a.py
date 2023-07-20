from collections import deque


def solve(n, s):

    P = list(s)
    Q = deque()
    res = False
    for _ in range(n-1):
        Q.appendleft(P.pop())
        tmp_p = ''.join(P)
        tmp_q = ''.join(Q)
        if tmp_p < tmp_q:
            res = True
    return res


T = int(input())
ans = []
for _ in range(T):
    N = int(input())
    S = input()
    r = 'No'
    if solve(N, S):
        r = 'Yes'
    ans.append(r)
print(*ans, sep="\n")
