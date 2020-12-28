n=int(input())
a,b,c=[],[],[]

for _ in range(n):
    a_i,b_i,c_i=map(int,input().split())

    a.append(a_i)
    b.append(b_i)
    c.append(c_i)

dp_a,dp_b,dp_c=[0]*(n+1),[0]*(n+1),[0]*(n+1)

for i in range(n+1):
    if i>0:
        dp_a[i]=max(dp_b[i-1]+a[i-1],dp_c[i-1]+a[i-1])
        dp_b[i]=max(dp_c[i-1]+b[i-1],dp_a[i-1]+b[i-1])
        dp_c[i]=max(dp_a[i-1]+c[i-1],dp_b[i-1]+c[i-1])


print(max(dp_a[n],dp_b[n],dp_c[n]))