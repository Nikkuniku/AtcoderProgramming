from collections import deque
from sys import stdin


def main():
    from builtins import input, int, map

    N = int(input())
    Edge = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, stdin.readline().split())
        u -= 1
        v -= 1
        Edge[u].append((v, w))
        Edge[v].append((u, w))
    P = [-1] * N  # P[i] はiの親。iが根なら-1
    Q = deque([0])  # queue。根にするやつを最初に追加
    R = []  # トポロジカルソート
    while Q:
        i = deque.popleft(Q)
        R.append(i)
        for a, w in Edge[i]:
            if a == P[i]:
                continue
            P[a] = i
            Edge[a].remove((i, w))  # ☆☆☆
            deque.append(Q, a)

    MOD = 10**9 + 7
    L = 60
    ans = 0
    pow2 = [pow(2, i, MOD) for i in range(L)]
    Vs = R[::-1]
    for i in range(L):
        dp = [0] * (2 * N)
        pow2val = pow2[i]
        for v in Vs:
            x, y, z = 0, 0, 0
            for j, w in Edge[v]:
                bit = (w >> i) & 1
                x = (x + dp[2 * j + bit] + 1 - bit) % MOD
                y = (y + dp[2 * j + (1 - bit)] + bit) % MOD
                z = (z + (dp[2 * j] + 1) * dp[2 * j + 1]) % MOD
            dp[2 * v] = x
            dp[2 * v + 1] = y
            ans = (
                ans
                + (pow2val * y) % MOD
                + (pow2val * (((x * y) % MOD - z) % MOD)) % MOD
            ) % MOD
    print(ans)


main()
