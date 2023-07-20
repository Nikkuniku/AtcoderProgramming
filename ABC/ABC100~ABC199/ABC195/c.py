N = int(input())
ans = 0
p = 3
cnt = 1
for i in range(10):
    l = pow(10, p)
    r = pow(10, p+3)-1
    if N < l:
        break
    ans += cnt*(min(r, N)-l+1)
    p += 3
    cnt += 1
print(ans)
