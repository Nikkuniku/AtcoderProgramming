s=list(input().split())
n=int(input())

m=len(s)

ng =[]
ng_jo=[]

if n==0:
    print(*s)
for _ in range(n):
    t=input()
    ng.append(t)

for l in ng:
    ng_jo.append(l.replace('*','[a-z]'))
import re

ans=[]
for i in range(m):
    j=0
    p=len(s[i])
    flg=0
    while j<len(ng):

        if s[i]==ng[j]:
            ans.append('*'*p)
            flg+=1
            break

        if re.fullmatch(ng[j].replace('*','[a-z]'),s[i]):
            ans.append('*'*p)
            flg+=1
            break
        
        if j==len(ng)-1 and flg==0:
            ans.append(s[i])
            break
        j+=1

print(*ans)
