n=int(input())
a=list(map(int,input().split()))
from collections import Counter
c=Counter(a)
cards=[]
for p in list(c.items()):
    if p[1]%2==0:
        cards.append([p[0],2])
    else:
        cards.append([p[0],1])
cards.sort(reverse=True,key=lambda x:x[1])
cnt=0
for p in cards:
    if p[1]==2:
        cnt+=1
ans=len(cards)
if cnt%2==1:
    ans-=1
print(ans)
