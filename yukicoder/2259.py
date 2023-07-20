L, R, C = map(int, input().split())
ans = 1 << 60
if R-L <= 1000:
    for x in range(L, R+1):
        tmp = x*C
        b = 1000*((tmp+1000-1)//1000)
        ans = min(ans,abs(b-tmp))
else:
    ans = 0
print(ans)
