n,k=map(int,input().split())
d={}
r=[0]
for _ in range(n):
    a,b=map(int,input().split())
    if a in d:
        d[a]+=b
    else:
        r.append(a)
        d[a]=b

now=0
money=k
next=1
r=sorted(r)
while True:
    nt=r[next]
    can=now+money
    if nt<=can:
        money-=(nt-now)
        money+=d[nt]
        now=nt
    else:
        now=now+money
        break
    next+=1

    if next>len(r)-1:
        now+=money
        break

print(now)