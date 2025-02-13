N = int(input())
l = 1
r = N
while r - l > 1:
    mid = (l + r) // 2
    print("?", mid, flush=True)
    S = int(input())
    if S == 0:
        l = mid
    else:
        r = mid
print("!", l)
