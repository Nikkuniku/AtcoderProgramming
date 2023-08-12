from collections import Counter
N, M = map(int, input().split())
A = [int(input())-1 for _ in range(N)]
b = [[0]*M for _ in range(N)]
d = Counter(A)
csum = [[0] for _ in range(M)]
for j in range(M):
    for i in range(N):
        csum[j].append(csum[j][-1]+(A[i] != j))

# 集合を表すbinから次にぬいぐるみを置く最初のインデックスを返す


def idx(bin):
    res = 0
    for i in range(M):
        if bin & (1 << i):
            res += d[i]
    return res

# あるぬいぐるみvをi番目の区画から並べる場合のコスト（元の配置と異なる数）を返す


def cost(v, i):
    return csum[v][i+d[v]]-csum[v][i]


INF = 1 << 62
dp = [INF]*(1 << M)
dp[0] = 0
for s in range(1 << M):
    for v in range(M):
        if s & (1 << v):
            continue
        dp[s | (1 << v)] = min(dp[s | (1 << v)], dp[s]+cost(v, idx(s)))

print(dp[-1])
