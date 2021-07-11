n,x=map(int,input().split())
a=list(map(int,input().split()))

for i in range(n):
    if i%2==1:
        a[i]-=1

s=sum(a)
ans='No'
if x>=s:
    ans='Yes'
print(ans)
