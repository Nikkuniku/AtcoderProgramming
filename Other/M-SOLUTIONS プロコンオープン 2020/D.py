n=int(input())
a=list(map(int,input().split()))

b=[0]

for i in range(1,n):
    if a[i]>a[i-1]:
        b.append(1)
    else:
        b.append(0)

ans=1000
for j in range(n-1):
    if b[j]==0:
        if b[j+1]==1:
            kabu=ans//a[j]

            ans+=(a[j+1]-a[j])*kabu
    else:
        if b[j+1]==1:
            kabu=ans//a[j]
            ans+=(a[j+1]-a[j])*kabu
print(ans)
