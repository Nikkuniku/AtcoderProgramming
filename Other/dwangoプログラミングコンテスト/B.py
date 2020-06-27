s=input()

arr=[]
flg=0
for i in range(1,len(s)):
    if flg==0:
        if s[i-1]=='2' and s[i]=='5':
            ans=1
            flg=1
        else:
            ans=0
            flg=0

        arr.append(ans)
    else:
        flg=0
        continue

from itertools import groupby

gr=groupby(arr)
ans=0

def keisan(n):
    return n*(n+1)//2


for _ ,group in gr:
    a=list(group)
    if a==[1]:
        ans+=1
    elif 0 in a:
        continue
    else:
        ans+=keisan(len(a))

print(ans)