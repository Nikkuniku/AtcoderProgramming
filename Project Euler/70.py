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


ans = 1 << 60
k = -1
L = 10000000
for i in range(2, L):
    A, B = [], []
    n = i
    phi = totient(i)
    val = i / phi
    while i > 0:
        A.append(i % 10)
        i //= 10
    while phi > 0:
        B.append(phi % 10)
        phi //= 10
    if len(A) != len(B):
        continue
    A.sort()
    B.sort()
    if A == B:
        if ans > val:
            ans = val
            k = n
print(k, ans)
