n,k=map(int,input().split())

div_k=[]
for i in range(1,n+1):
    if i%k==0:
        div_k.append(i)

ans=pow(len(div_k),3)

if k%2==0:
    div_2k=[]
    for j in range(1,n+1):
        if j%k==k//2:
            div_2k.append(i)

    ans+=pow(len(div_2k),3)


print(ans)