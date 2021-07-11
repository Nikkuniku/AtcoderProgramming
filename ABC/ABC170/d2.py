n=int(input())
a=list(map(int,input().split()))
a=sorted(a)
p=max(a)
div=[0]*(p+1)

# # 同じものを探す
from collections import Counter
c= Counter(a)
for q in a:
    if c[q]>1 and div[q]==0:
        j=q
        while j<=p:
            div[j]+=1
            j+=q     

ans=0
for i in range(n):
    if div[a[i]]==0:
        ans+=1

        j=a[i]
        while j<=p:
            div[j]+=1
            j+=a[i]

print(ans)