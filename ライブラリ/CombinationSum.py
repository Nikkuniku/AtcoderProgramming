def CombSum(input_array: list, r: int) -> int:
    '''
    N個の値からr個選んだ時の組み合わせの積の総和
    余りは998244353(MODに格納)

    Parameters
    ----------
    input_array:list
        入力配列（長さ:5000まで）
    r:int
        r個選ぶ。配列サイズ:Nのとき、r<=N.
    '''
    n = len(input_array)
    dp = [[0]*(n+1) for _ in range(n+1)]
    MOD = 998244353
    for i in range(n):
        dp[i][0] = 1
    for i in range(n):
        for j in range(1, n+1):
            dp[i+1][j] = dp[i][j]+dp[i][j-1]*input_array[i]
            dp[i+1][j] %= MOD
    return dp[n][r]


# 使用例
a = list(map(int, input().split()))
r = int(input())
print(CombSum(a, r))
