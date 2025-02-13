# 2分探索で以下の条件を満たすmを返す。
# 見つからない場合はNoneを返す
#    f(m) = n, m < [0, n]
# 巨大なnにも対応。これはbisectではできない。
def bisearch(f, n):
    l = 0
    r = n
    fl = f(l)
    fr = f(r)
    while l <= r:
        m = (l + r) // 2
        fm = f(m)
        # print l,m,r,fl,fm,fr,n
        if fm == n:
            return m
        elif fm > n:
            r = m - 1
            fr = f(r)
        else:
            l = m + 1
            fl = f(l)


def try_square_root(n2):
    return bisearch(lambda n: n * n, n2)


L = 10**12
a = [1, 3]
b = [0, 1]
for i in range(20):
    p = 6 * a[-1] - a[-2] - 2
    q = 6 * b[-1] - b[-2]
    a.append(p)
    b.append(q)
    if p + q > L:
        exit(print(p, q))
