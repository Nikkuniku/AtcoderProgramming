n, l, r = map(int, input().split())


def solve2():
    ans = 0
    for i in range(1, r+1):
        if (i ^ n) < n:
            ans += 1
    return ans


def cnt(x):
    tmp = 0
    re = 0
    for i in range(60, -1, -1):
        if (n >> i) & 1:
            tmp2 = pow(2, i+1)-1
            tmp = pow(2, i)
            if tmp <= x <= tmp2:
                re += (x-tmp+1)
            elif tmp2 <= x:
                re += (tmp2-tmp+1)
    return re


print(cnt(r)-cnt(l-1))
