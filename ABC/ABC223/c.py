n=int(input())
a=[]
b=[]
for _ in range(n):
    a_i,b_i=map(int,input().split())
    a.append(a_i)
    b.append(b_i)

c=[]
for i in range(n):
    c.append(a[i]/b[i])
t=sum(c)/2

ans=0
for i in range(n):
    if t>=c[i]:
        t-=c[i]
        ans+=a[i]
    else:
        ans+=b[i]*t
        break
print(ans)