def LIS(input_array: list) -> int:
    """
    配列のLISの長さを返す。

    Parameters
    ----------
    input_array:list
    """
    from bisect import bisect_left

    INF = 1 << 62
    dp = [INF] * len(input_array)
    for c in input_array:
        dp[bisect_left(dp, c)] = c
    ans = bisect_left(dp, INF)
    # return (ans, dp[:ans])
    return ans


N = int(input())
C = []
for _ in range(N):
    x, r = map(int, input().split())
    C.append((x - r, x + r))
C.sort(key=lambda x: x[1])
C.sort(key=lambda x: x[0])
C = C[::-1]
P = [d for c, d in C]

print(LIS(P))
