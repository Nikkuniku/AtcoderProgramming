def extGCD(a: int, b: int) -> tuple:
    '''
    拡張ユークリッドの互除法
    d=GCD(a,b)とした時
    一次不定方程式ax+by=d
    の解(x,y,d)を返す

    Parameters
    ----------
    a:int
    b:int
    '''
    if b == 0:
        return 1, 0, a
    q, r = a//b, a % b
    s, t, d = extGCD(b, r)
    x, y = t, s-q*t
    return x, y, d


a, b = map(int, input().split())
res = extGCD(a, b)
print(res)
