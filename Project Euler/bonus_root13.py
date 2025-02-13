def extraction_of_square_root(n: int, precision: int = 0) -> tuple:
    """
    nの平方根を開平法で求める。
    precisionは小数の桁数に対応する。

    Parameters
    ----------
    n:int
        平方根の計算対象
    precision:int
        求める平方根の小数精度

    Returns
    -------
    Integer :list of int
        求めた平方根の整数部分の配列
    decimals:list of int
        求めた平方根の小数部分の配列

    See Also
    --------
    https://manabitimes.jp/math/1318 : 参考文献
    """
    digit = []
    while n > 0:
        digit.append(n % 10)
        n //= 10
    digit = digit[::-1]
    s = digit[0]
    if len(digit) % 2 == 0:
        s = 10 * digit[0] + digit[1]
    l = 1
    r = s * s
    while r - l > 1:
        mid = (l + r) // 2
        if mid * mid <= s:
            l = mid
        else:
            r = mid
    k = l
    Integer = [k]
    L = k + k
    R = s - k * k
    i = 2
    if len(digit) % 2 == 0:
        i = 3
    while i <= len(digit) - 1:
        x = 100 * R + 10 * digit[i - 1] + digit[i]
        for p in range(9, -1, -1):
            y = 10 * L + p
            if y * p <= x:
                Integer.append(p)
                break
        R = x - (10 * L + p) * p
        L = (10 * L + p) + p
        i += 2
    decimals = []
    for _ in range(precision):
        x = 100 * R
        for p in range(9, -1, -1):
            y = 10 * L + p
            if y * p <= x:
                decimals.append(p)
                break
        R = x - (10 * L + p) * p
        L = (10 * L + p) + p
    return Integer, decimals


N = 13
M = 1000
Integer, decimals = extraction_of_square_root(N, M)
ans = sum(decimals)
print(ans)
