n=int(input())
a=list(map(int,input().split()))
ans=[0]*n
totals=[0]*n

for i in range(n-1,-1,-1):
    if totals[i]%2==a[i]:
        continue
    else:
        ans[i]+=1
        tmp=1
        while tmp*tmp<=i+1:
            if (i+1)%tmp==0:
                totals[tmp-1]+=1
                if tmp !=(i+1)//tmp:
                    totals[((i+1)//tmp)-1]+=1

            tmp+=1


cnt=ans.count(1)

print(cnt)
if cnt!=0:
    b=[]
    for j in range(n):
        if ans[j]==1:
            b.append(j+1)

    print(*b)
    