N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(A)[::-1][:K]
print(*B, sep="\n")
print(*[format(b, '010b') for b in B], sep="\n")
lim = 10
l = 0
r = 500


def isOK(s):
    C = B[:]
    Flg = [False]*K
    cnt = 0
    print(format(s, '010b'))
    for i in range(lim, -1, -1):
        if not s & (1 << i):
            continue
        for j in range(K):
            if C[j] & (1 << i):
                C[j]|=(1<<i)
                continue
            p=1<<i
            q=(1<<i)-1
            r=B[j]&q
            cnt+=p-r
    if cnt <= M:
        return True
    return False


while r-l > 1:
    mid = (l+r)//2

    if isOK(mid):
        l = mid
    else:
        r = mid

print(r)
