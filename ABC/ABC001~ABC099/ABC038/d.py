from collections import defaultdict


def LIS(input_array: list) -> int:
    '''
    配列のLISの長さを返す。

    Parameters
    ----------
    input_array:list
    '''
    from bisect import bisect_left
    INF = 1 << 62
    dp = [INF]*len(input_array)
    for c in input_array:
        dp[bisect_left(dp, c)] = c
    ans = bisect_left(dp, INF)
    # return (ans, dp[:ans])
    return ans


N = int(input())
d = defaultdict(list)
for _ in range(N):
    a, b = map(int, input().split())
    d[a].append(b)
p = sorted(list(d.items()))
Q = []
for c in p:
    Q += sorted(c[1], reverse=True)
ans = LIS(Q)
print(ans)
