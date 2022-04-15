def polydiv(xs, ys):
    xn = len(xs)
    yn = len(ys)
    zs = xs.copy()
    qs = []
    for _ in range(xn - yn + 1):
        temp = zs[0] // ys[0]
        for i in range(yn):
           zs[i] -= temp * ys[i]
        qs.append(temp)
        zs = zs[1:]
    if qs == []: qs = [0.]
    return qs

n,m=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
a=list(reversed(a))
c=list(reversed(c))
ans=[]
p=polydiv(c,a)
for i in range(len(p)):
    ans.append(int(p[i]))
ans=list(reversed(ans))
print(*ans)