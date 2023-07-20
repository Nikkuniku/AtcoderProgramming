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
    x, y, u, v = 1, 0, 0, 1
    while b > 0:
        k = a//b
        x -= k*u
        y -= k*v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    return x, y, a


a, b = map(int, input().split())
res = extGCD(a, b)
print(*res[:2])
