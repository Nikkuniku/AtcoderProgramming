def popcount(x):
    """xの立っているビット数をカウントする関数
    (xは64bit整数)"""

    # 2bitごとの組に分け、立っているビット数を2bitで表現する
    x = x - ((x >> 1) & 0x5555555555555555)

    # 4bit整数に 上位2bit + 下位2bit を計算した値を入れる
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)

    x = (x + (x >> 4)) & 0x0F0F0F0F0F0F0F0F  # 8bitごと
    x = x + (x >> 8)  # 16bitごと
    x = x + (x >> 16)  # 32bitごと
    x = x + (x >> 32)  # 64bitごと = 全部の合計
    return x & 0x0000007F


from collections import defaultdict

N, L, K = map(int, input().split())
S = [list(input()) for _ in range(N)]
ans = 0
for s in range(1 << L):
    if popcount(s) != L - K:
        continue
    d = defaultdict(int)
    res = 0
    for i in range(N):
        tmp = []
        for j in range(L):
            if s & (1 << j):
                tmp.append(S[i][j])
        tmp_s = "".join(tmp)
        d[tmp_s] += 1
        res = max(res, d[tmp_s])
    ans = max(ans, res)
print(ans)
