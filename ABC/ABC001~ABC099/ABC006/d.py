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
C = [int(input()) for _ in range(N)]
ans = N - LIS(C)
print(ans)
