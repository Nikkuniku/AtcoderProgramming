num=[i for i in range(1,11)]
n=len(num)

ans=0
for i in range(1<<n):
    tmp=0
    for j in range(n):
        if (i>>j)&1:
            tmp+=num[j]
    
    if tmp%2==1:
        ans+=1
print(ans)
print(num)