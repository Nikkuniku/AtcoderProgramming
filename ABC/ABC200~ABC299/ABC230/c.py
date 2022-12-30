n,a,b=map(int,input().split())
p,q,r,s=map(int,input().split())

ans=[['.']*(s-r+1) for _ in range(q-p+1)]


for i in range(p,q+1):
    for j in range(r,s+1):
        if i-a==j-b:   
            k=i-a
            if max(1-a,1-b)<=k<=min(n-a,n-b):
                ans[i-p][j-r]='#'
        elif i-a==-(j-b):
            k=i-a
            if max(1-a,b-n)<=k<=min(n-a,b-1):
                ans[i-p][j-r]='#'

for i in range(len(ans)):
    print(''.join(ans[i]))
