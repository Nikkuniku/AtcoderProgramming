from bisect import bisect_left
x, y, z, K = map(int, input().split())
cakes = [list(map(int, input().split())) for _ in range(3)]
ab = []
for a in cakes[0]:
    for b in cakes[1]:
        ab.append(a+b)
ab.sort()


def check(m):
    cnt = 0
    for c in cakes[2]:
        idx = bisect_left(ab, m-c)
        cnt += len(ab)-idx
    re = False
    if cnt >= K:
        re = True

    return re


l = -1
r = 3*10**10+3
while r-l > 1:
    mid = (l+r)//2
    if check(mid):
        l = mid
    else:
        r = mid
ans = []
ab = ab[::-1]
for c in cakes[2]:
    for abi in ab:
        if c+abi < l:
            break
        ans.append(abi+c)
ans += [l]*(K-len(ans))
ans = sorted(ans)[::-1][:K]
print(*ans, sep="\n")
