n, m, d = map(int, input().split())
p = 2*(n-d)/(n**2)
if d == 0:
    p = 1/n
ans = (m-1)*p
print(ans)
