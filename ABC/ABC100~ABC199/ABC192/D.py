X = input()
M = int(input())


def f(k):
    X_tmp = X[::-1]
    res = sum([pow(k, i)*int(X_tmp[i]) for i in range(len(X_tmp))])
    return res


ans = 0
if len(X) == 1:
    if int(X) <= M:
        ans = 1
    print(ans)
    exit()
d = max([int(x) for x in list(X)])
l = 0
r = 1 << 60
while r-l > 1:
    mid = (l+r)//2
    if f(mid) <= M:
        l = mid
    else:
        r = mid
ans = max(r-1-(d+1)+1, 0)
print(ans)
