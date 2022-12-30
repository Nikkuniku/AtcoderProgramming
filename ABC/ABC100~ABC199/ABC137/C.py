N=int(input())

from collections import Counter

ans=[]
d={}
cnt=0
for i in range(N):
    s=list(input())
    s=sorted(s)
    
    s= ''.join(s)

    if s in d:
        d[s]+=1
    else:
        d[s]=1

total=0

for _,value in d.items():
    if value==1:
        continue
    else:
        total +=value*(value-1)/2

print(int(total))