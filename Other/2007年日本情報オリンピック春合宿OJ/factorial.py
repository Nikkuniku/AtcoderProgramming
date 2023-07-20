def factorization(n: int) -> list:
    '''
    2以上の整数n => [[素因数, 指数], ...]の2次元リスト

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

    return arr


N = int(input())
factor = factorization(N)


def judge(k):
    res = True
    for p, e in factor:
        cnt = 0
        i = 1
        while k//pow(p, i) > 0:
            cnt += k//pow(p, i)
            i += 1
        if cnt < e:
            res = False
    return res


l = 0
r = N
while r-l > 1:
    mid = (l+r)//2
    if judge(mid):
        r = mid
    else:
        l = mid
ans = r
print(ans)
