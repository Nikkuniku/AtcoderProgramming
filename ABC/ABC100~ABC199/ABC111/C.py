n=int(input())
a=list(map(int,input().split()))

odd={}
even={}
total={}

for i in range(n):
    t=a[i]
    if i%2==0:
        if t in odd:
            odd[t]+=1
        else:
            odd[t]=1
    else:
        if t in even:
            even[t]+=1
        else:
            even[t]=1
    if t in total:
        total[t]+=1
    else:
        total[t]=1

odd=sorted(odd.items(),key=lambda x: x[1],reverse=True)
even=sorted(even.items(),key=lambda x: x[1],reverse=True)
if len(total)==1:
    print(n//2)
    exit(0)
ans=n
cnt1=0
for i in odd:
    if cnt1==2:
        break
    cnt2=0
    for j in even:
        if cnt2==2 or i[0]==j[0]:
            continue
    
        ans=min(ans,n-i[1]-j[1])
        cnt2+=1
    cnt1+=1

print(ans)