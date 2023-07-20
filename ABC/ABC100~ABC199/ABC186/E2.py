from math import gcd


def totient(n: int) -> int:
    '''
    オイラーのphi関数
    1以上n以下の数でnと互いに素な数の個数
    Parameters
    ----------
    n:int
    '''
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
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
        res = res*(p-1)//p
    return res


def solve(N, S, K):
    g = gcd(N, K)
    res = -1
    if S % g != 0:
        return res
    N //= g
    S //= g
    K //= g
    invK = pow(K, totient(N)-1, N)
    res = (invK*(-S)) % N
    return res


T = int(input())
ans = []
for _ in range(T):
    N, S, K = map(int, input().split())
    ans.append(solve(N, S, K))
print(*ans, sep="\n")
