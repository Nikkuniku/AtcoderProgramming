n=int(input())
a=list(map(int,input().split()))

hat = [0,0,0]

mod = 10**9 + 7

ans=1

for i in range(n):
    tmp=0
    index=0
    for j,k in enumerate(hat):
        if k==a[i]:
            tmp+=1
            index=j

    ans = (ans*tmp)%mod

    hat[index]+=1

print(ans)

