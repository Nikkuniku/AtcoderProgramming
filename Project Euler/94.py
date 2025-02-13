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


L = 1000_000_000
ans = 0
# x,x,x-1の形
for x in range(1, L):
    if x + x + x - 1 > L:
        break
    if x - 1 <= 0:
        continue
    if x % 4 == 0 or x % 4 == 2:
        continue
    t = (x + 1) * (3 * x - 1) // 4
    square_root = try_square_root(t)
    if square_root == None:
        continue
    ans += x + x + x - 1
    print(x, x, x - 1)

# x,x,x+1の形
for x in range(1, L):
    if x + x + x + 1 > L:
        break
    if x % 4 == 0 or x % 4 == 2:
        continue
    t = (x - 1) * (3 * x + 1) // 4
    square_root = try_square_root(t)
    if square_root == None:
        continue
    ans += x + x + x + 1
    print(x, x, x + 1)
print(ans)
