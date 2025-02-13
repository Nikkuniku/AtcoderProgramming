N, C = map(int, input().split())
X, V = [0], [0]
for _ in range(N):
    x, v = map(int, input().split())
    X.append(x)
    V.append(v)
from itertools import accumulate

revX = list(map(lambda x: C - x, X))[::-1]
revX.pop()
revV = list(accumulate(V[::-1]))
revV.pop()
cumV = list(accumulate(V))
cum1 = []
cum2 = []
for i in range(N + 1):
    tmp1 = cumV[i] - 2 * X[i]
    if cum1:
        if cum1[-1] < tmp1:
            cum1.append(tmp1)
        else:
            cum1.append(cum1[-1])
    else:
        cum1.append(tmp1)
    tmp2 = cumV[i] - X[i]
    if cum2:
        if cum2[-1] < tmp2:
            cum2.append(tmp2)
        else:
            cum2.append(cum2[-1])
    else:
        cum2.append(tmp2)
# 時計回りでの最大値
ans = cum2[-1]
# 反時計回りでの最大値
for i in range(N):
    ans = max(ans, revV[i] - revX[i])
# 反時計回りと時計回りの組み合わせ
for l in range(N):
    # 時計->反時計回り
    tmp_pattern1 = cum1[N - 1 - l] + revV[l] - revX[l]
    # 反時計->時計
    tmp_pattern2 = cum2[N - 1 - l] + revV[l] - 2 * revX[l]
    ans = max(ans, tmp_pattern1, tmp_pattern2)
print(ans)
