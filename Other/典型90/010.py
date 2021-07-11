n=int(input())
a=[0]*n
b=[0]*n

for i in range(n):
    c,p=map(int,input().split())
    if c==1:
        a[i]=p
    else:
        b[i]=p

cum_a=[0]
cum_b=[0]

for j in range(n):
    cum_a.append(cum_a[-1]+a[j])
    cum_b.append(cum_b[-1]+b[j])

q=int(input())
for _ in range(q):
    l,r=map(int,input().split())

    ans1=cum_a[r]-cum_a[l-1]
    ans2=cum_b[r]-cum_b[l-1]

    print(ans1,ans2)

