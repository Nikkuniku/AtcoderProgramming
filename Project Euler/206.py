from sys import setrecursionlimit

setrecursionlimit(10**9)


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


def MakeNum(A):
    res = 0
    for a in A:
        res *= 10
        res += a
    return res


def dfs(A=[]):
    if len(A) == 9:
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        v = 0
        for i in range(19):
            v *= 10
            if i % 2 == 0:
                v += digits[i // 2]
            else:
                v += A[i // 2]
        temp = v
        root = try_square_root(temp)
        if root != None:
            print(root**2)
            exit(print(root))
        return
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]:
        A.append(i)
        dfs(A)
        A.pop()


dfs()
