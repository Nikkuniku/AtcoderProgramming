n = int(input())


def cal(s):
    return (n+1)*(n+2)//2 - s*(s-1)//2


l = -1
r = n+3

while r-l > 1:
    mid = (r+l)//2

    if cal(mid) >= n*(n+1)//2:
        l = mid
    else:
        r = mid

print(n-l+2)
