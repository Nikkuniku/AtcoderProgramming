n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab = [[a[i], b[i]] for i in range(n)]
ab.sort(key=lambda x: x[0])
b = [ab[i][1] for i in range(n)]


def LIS(input_array: list) -> int:
    '''
    配列aのLISの長さを返す。

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


ans = n+LIS(b)
print(ans)
