N = int(input())


def re(a, b, c):
    return (a*b+a*c+b*c)/(a*b*c)


exit_FLG = False
for h in range(1, 3501):
    for n in range(1, 3501):
        l = 0
        r = 3600

        while r-l > 1:
            mid = (r+l)//2

            if 4/N >= re(h, n, mid):
                r = mid
            else:
                l = mid

        if 4/N == re(h, n, r):
            exit_FLG = True
            break

    if exit_FLG:
        break
print(h, n, r)
