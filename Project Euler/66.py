def cfsqrt(m):
    n0 = int(m ** (1 / 2))
    if n0 * n0 == m:
        return [n0]
    n, a, b, cf = n0, 1, 0, []
    while True:
        b = n * a - b
        a = (m - b * b) // a
        n = (n0 + b) // a
        cf.append(n)
        if a == 1:
            break
    return [n0, cf]


def Approximate_fraction_ByContinued_Fraction(input_array: list):
    """
    連分数展開された配列から近似分数p/qを返す。

    Parameters
    ----------
    input_array:list
    """
    pn, qn = input_array[0], 1
    pn_1, qn_1 = -1, -1
    pn_2, qn_2 = -1, -1
    for i in range(1, len(input_array)):
        pn_2, qn_2 = pn_1, qn_1
        pn_1, qn_1 = pn, qn
        if i == 1:
            pn = input_array[i - 1] * input_array[i] + 1
            qn = input_array[i]
        else:
            pn = input_array[i] * pn + pn_2
            qn = input_array[i] * qn + qn_2
    return pn, qn


N = 1000
ans = []
for d in range(2, N + 1):
    res = cfsqrt(d)
    if len(res) == 1:
        continue
    period = [res[0]]
    for j, p in enumerate(res[1]):
        if j == len(res[1]) - 1:
            continue
        period.append(p)
    if len(res[1]) % 2 == 0:
        p, q = Approximate_fraction_ByContinued_Fraction(period)
        ans.append((d, p))
    else:
        p, q = Approximate_fraction_ByContinued_Fraction(period)
        X = p * p + d * q * q
        ans.append((d, X))
ans.sort(key=lambda x: x[1], reverse=True)
print(ans[0])
print(ans[0][0])
