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


def make(x, y, C, K, a, b):
    X, Y = 0, 0
    for i in range(60):
        if C & (1 << i):
            if x:
                X |= 1 << i
                x -= 1
            elif y:
                Y |= 1 << i
                y -= 1
    for i in range(60):
        if not (C & (1 << i)):
            if K:
                X |= 1 << i
                Y |= 1 << i
                K -= 1
    if K > 0:
        return False, -1, -1
    if X >= pow(2, 60) or Y >= pow(2, 60) or X ^ Y != C:
        return False, -1, -1
    if popcount(X) != a or popcount(Y) != b:
        return False, -1, -1
    return True, X, Y


a, b, C = map(int, input().split())
D = popcount(C)
for x in range(D + 1):
    y = D - x
    isOK, X, Y = make(x, y, C, a - x, a, b)
    if isOK:
        exit(print(X, Y))
print(-1)
