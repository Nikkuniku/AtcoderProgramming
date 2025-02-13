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


def solve(n, m):
    res = 0
    MOD = 998244353
    for i in range(n):
        tmp = i & m
        res += popcount(tmp)
        res %= MOD
    return res


def solve2(N, M):
    ans = 0
    MOD = 998244353
    for i in range(61):
        if M & (1 << i) == 0:
            continue
        ans += pow(2, i, MOD) * (N // pow(2, i + 1))
        k = max((N % pow(2, i + 1)) - pow(2, i), 0)
        ans += k
        ans %= MOD
    return ans


c = 8388607
a, b = c, c
print(solve(a, b))
print(solve2(a, b))
