n,c=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))

ans=10**8
for i in range(1,11):
    for j in range(1,11):
        if i==j:continue

        tmp=0
        for k in range(n):
            if k%2==0:
                if a[k]!=i:
                    tmp+=c
            else:
                if a[k]!=j:
                    tmp+=c

        ans=min(ans,tmp)
print(ans)