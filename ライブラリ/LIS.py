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


def minimum_LIS(input_array: list) -> list:
    '''
    配列のLISのうち、辞書順最小のLISを返す。

    Parameters
    ----------
    input_array:list
    '''
    from bisect import bisect_left
    INF = 1 << 62
    n = len(input_array)
    dp = [INF]*n
    pos = [-1]*n
    for i, v in enumerate(input_array):
        dp[bisect_left(dp, v)] = v
        pos[i] = bisect_left(dp, v)
    k = bisect_left(dp, INF)-1
    ans = []
    for i in range(n-1, -1, -1):
        if pos[i] == k:
            k -= 1
            ans.append(input_array[i])

    return (len(ans), ans[::-1])


n = int(input())
a = list(map(int, input().split()))

print(LIS(a))
print(minimum_LIS(a))
