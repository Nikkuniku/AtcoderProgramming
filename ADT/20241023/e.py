def LCS(s: str, t: str) -> str:
    """
    2つの文字列s,tの最長共通部分列を返す.
    Parameters
    ----------
    s:string
    t:string
    """
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
            if s[i] == t[j]:
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
    # 復元
    i = n
    j = m
    tmp = []
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        elif dp[i][j] == dp[i - 1][j - 1]:
            i -= 1
            j -= 1
        else:
            i -= 1
            j -= 1
            tmp.append(s[i])
    re = "".join(tmp[::-1])

    return re


S = input().upper()
T = input()

ans = "No"
if T[-1] != "X":
    L = LCS(S, T)
    if len(L) == 3:
        ans = "Yes"
else:
    L = LCS(S, T[:2])
    if len(L) == 2:
        ans = "Yes"
print(ans)
