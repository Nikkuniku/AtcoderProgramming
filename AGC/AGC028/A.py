n,m=map(int,input().split())
s=input()
t=input()

from fractions import gcd

lcm=n*m//gcd(n,m)

if s[0]!=t[0]:
    print(-1)
    exit(0)

ans=lcm
# sについて
dn={}
for i in range(n):
    if i==0:
        dn[1]=s[i]
    else:
        dn[i*int((lcm)/n) +1]=s[i]

for j in range(m):
    if j==0:
        continue
    else:
        k = j*int(lcm/m) + 1

        if k in dn:
            if dn[k]!=t[j]:
                ans=-1
        else:
            dn[k]=t[j]

print(ans)



