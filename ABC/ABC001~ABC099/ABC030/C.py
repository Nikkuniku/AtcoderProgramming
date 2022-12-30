n,m=map(int,input().split())
x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))


cnt=0
now_a=0
i=0
j=0

t=a[0]
while i<=n and j<=m:
    if now_a==0:
        if i<n and  t<=a[i]:
            t=a[i]+x
            now_a=1
        i+=1
    else:
        if j<m and t<=b[j] :
            t=b[j]+y
            now_a=0
            cnt+=1
        j+=1

print(cnt)