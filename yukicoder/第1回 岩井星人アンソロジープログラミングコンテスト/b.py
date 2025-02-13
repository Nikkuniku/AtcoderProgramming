l = 0
r = 10**9 + 1
M = 30
while r - l > 1:
    mid = (l + r) // 2
    print(mid, flush=True)
    s = int(input())
    if s == 1:
        exit()
    else:
        r = mid
