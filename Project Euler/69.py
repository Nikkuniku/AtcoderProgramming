def totient(n: int) -> int:
    """
    オイラーのphi関数
    1以上n以下の数でnと互いに素な数の個数
    Parameters
    ----------
    n:int
    """
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append((i, cnt))

    if temp != 1:
        arr.append((temp, 1))

    if arr == []:
        arr.append((n, 1))
    res = n
    for p, _ in arr:
        res = res * (p - 1) // p
    return res


ans = 0
k = -1
L = 10
for i in range(2, L + 1):
    phi = totient(i)
    if ans < i / phi:
        ans = i / phi
        k = i
print(k, ans)
