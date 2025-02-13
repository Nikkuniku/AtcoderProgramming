# i mod 10でSiを選択したとき、しない時の遷移先を考える
# まず以下のように定義する
# True：高橋君の勝ち（青木君の負け）
# False：高橋君の負け（青木君の勝ち）
# 高橋君のターンで、遷移先の候補にTrueとなるものが一つでもあれば、True
# 一つも存在しない場合は、False
# 青木君のターンで、遷移先の候補にFalseとなるものが一つでもあれば、False
# 全てTrueの場合はTrue
N = int(input())
S = input()
X = input()
dp = [[False] * 10 for _ in range(N + 1)]
dp[-1][0] = dp[-1][7] = True
pows = [pow(10, j, 7) for j in range(N)]
for i in range(N - 1, -1, -1):
    turn = X[i]
    s = int(S[i])
    for m in range(10):
        p = (m + pows[N - 1 - i] * s) % 7
        if turn == "T":
            dp[i][m] = dp[i + 1][p] | dp[i + 1][m]
        else:
            dp[i][m] = dp[i + 1][p] & dp[i + 1][m]
res = dp[0][0]
ans = "Takahashi" if res else "Aoki"
print(ans)
